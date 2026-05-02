# Implementation Plan: --write-docs Feature for Python (watsonx.ai Integration)

## Overview
Implement the `--write-docs` flag for Python files only, using watsonx.ai's granite-3-8b-instruct model to generate Google-style docstrings for undocumented functions, methods, and classes.

## Architecture

### Component Structure
```
codebase-scanner/
├── writers/                          # NEW: Documentation writers
│   ├── __init__.py
│   ├── base_writer.py               # Abstract base class
│   ├── watsonx_client.py            # watsonx.ai API client
│   ├── python_writer.py             # Google-style docstrings with AI
│   └── doc_inserter.py              # File modification engine
├── core/
│   └── doc_generator.py             # NEW: Orchestrates documentation generation
├── scanner.py                        # MODIFY: Add --write-docs flag
├── .env.example                      # NEW: Environment variable template
└── .gitignore                        # MODIFY: Add .env
```

## Implementation Details

### 1. Environment Configuration

**File: `.env.example`**
```bash
# watsonx.ai API Configuration
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
```

**Update `.gitignore`**
```
.env
*.bak
```

### 2. watsonx.ai API Client

**File: `writers/watsonx_client.py`**

**Purpose**: Handle all interactions with watsonx.ai REST API

**Key Features**:
- Load credentials from environment variables
- Generate docstrings using granite-3-8b-instruct model
- Handle API errors and rate limiting
- Retry logic for transient failures
- Token usage tracking

**API Request Format**:
```python
{
    "model_id": "ibm/granite-3-8b-instruct",
    "input": "<prompt>",
    "parameters": {
        "max_new_tokens": 500,
        "temperature": 0.3,
        "top_p": 0.9,
        "repetition_penalty": 1.1
    },
    "project_id": "<project_id>"
}
```

**Prompt Template**:
```
Generate a Google-style Python docstring for the following function.
Include Args, Returns, and Raises sections as appropriate.
Do not include placeholder text or TODO comments.

Function signature:
{function_signature}

Function body:
{function_body}

Generate ONLY the docstring content (without the triple quotes).
```

### 3. Base Documentation Writer

**File: `writers/base_writer.py`**

**Abstract Methods**:
- `generate_function_doc(func_info: Dict) -> str`
- `generate_method_doc(method_info: Dict, class_name: str) -> str`
- `generate_class_doc(class_info: Dict) -> str`
- `get_doc_start_marker() -> str`
- `get_doc_end_marker() -> str`
- `format_doc_line(line: str) -> str`

**Concrete Methods**:
- `validate_documentation(doc: str) -> bool`: Ensure no placeholders
- `extract_function_context(file_content: str, line_start: int, line_end: int) -> str`

### 4. Python Documentation Writer

**File: `writers/python_writer.py`**

**Key Methods**:
```python
class PythonDocumentationWriter(BaseDocumentationWriter):
    def __init__(self, watsonx_client: WatsonxClient):
        self.watsonx_client = watsonx_client
    
    def generate_function_doc(self, func_info: Dict, file_content: str) -> str:
        """Generate Google-style docstring using watsonx.ai"""
        # Extract function signature and body
        signature = self._extract_signature(func_info, file_content)
        body = self._extract_body(func_info, file_content)
        
        # Call watsonx.ai API
        docstring = self.watsonx_client.generate_docstring(
            signature=signature,
            body=body,
            function_name=func_info['name']
        )
        
        # Validate and format
        if self.validate_documentation(docstring):
            return self._format_docstring(docstring)
        else:
            raise ValueError("Generated docstring contains placeholders")
    
    def generate_class_doc(self, class_info: Dict, file_content: str) -> str:
        """Generate class-level docstring"""
        # Similar to function doc but with class context
        pass
    
    def generate_method_doc(self, method_info: Dict, class_name: str, file_content: str) -> str:
        """Generate method docstring with class context"""
        pass
```

**Docstring Format**:
```python
"""Brief one-line description.

Detailed description if needed (optional).

Args:
    param_name (type): Description of parameter
    another_param (type, optional): Description. Defaults to value.

Returns:
    return_type: Description of return value

Raises:
    ExceptionType: When this exception occurs
"""
```

### 5. Documentation Inserter

**File: `writers/doc_inserter.py`**

**Key Methods**:
```python
class DocumentationInserter:
    def insert_documentation(
        self, 
        file_path: Path, 
        doc_items: List[DocItem],
        create_backup: bool = True
    ) -> InsertionResult:
        """Safely insert documentation into source file"""
        # 1. Create backup
        if create_backup:
            backup_path = self.create_backup(file_path)
        
        try:
            # 2. Read file
            content = self._read_file(file_path)
            lines = content.splitlines(keepends=True)
            
            # 3. Sort items by line number (descending) to avoid offset issues
            sorted_items = sorted(doc_items, key=lambda x: x.line_start, reverse=True)
            
            # 4. Insert each docstring
            for item in sorted_items:
                indentation = self._get_indentation(lines, item.line_start)
                formatted_doc = self._format_with_indentation(item.docstring, indentation)
                lines.insert(item.line_start, formatted_doc)
            
            # 5. Write to temp file
            temp_path = file_path.with_suffix('.tmp')
            self._write_file(temp_path, ''.join(lines))
            
            # 6. Validate syntax
            if self.validate_python_syntax(temp_path):
                # 7. Atomic replace
                temp_path.replace(file_path)
                return InsertionResult(success=True, items_inserted=len(doc_items))
            else:
                raise SyntaxError("Generated code has syntax errors")
                
        except Exception as e:
            # Restore from backup
            if create_backup:
                self.restore_backup(backup_path, file_path)
            raise
    
    def validate_python_syntax(self, file_path: Path) -> bool:
        """Validate Python file syntax"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                ast.parse(f.read())
            return True
        except SyntaxError:
            return False
```

**Safety Features**:
- Create `.bak` backup before modification
- Validate syntax after insertion
- Atomic file operations (temp file + rename)
- Automatic rollback on errors
- Preserve file permissions and encoding

### 6. Documentation Generator

**File: `core/doc_generator.py`**

**Key Methods**:
```python
class DocumentationGenerator:
    def __init__(
        self,
        logger,
        watsonx_client: WatsonxClient,
        dry_run: bool = False,
        create_backup: bool = True,
        min_coverage: float = 80.0
    ):
        self.logger = logger
        self.watsonx_client = watsonx_client
        self.dry_run = dry_run
        self.create_backup = create_backup
        self.min_coverage = min_coverage
        self.python_writer = PythonDocumentationWriter(watsonx_client)
        self.inserter = DocumentationInserter()
    
    def generate_documentation(
        self, 
        scan_results: Dict, 
        config: Dict
    ) -> GenerationReport:
        """Main orchestration method"""
        report = GenerationReport()
        
        # Filter for Python files with undocumented items
        python_files = self._filter_python_files(scan_results)
        undocumented_files = self._filter_undocumented(python_files)
        
        self.logger.info(f"Found {len(undocumented_files)} Python files with undocumented items")
        
        for file_data in undocumented_files:
            file_report = self._process_file(file_data)
            report.add_file_report(file_report)
        
        return report
    
    def _process_file(self, file_data: Dict) -> FileReport:
        """Process a single file"""
        file_path = Path(file_data['file_path'])
        self.logger.info(f"Processing {file_path}")
        
        # Read file content
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        # Collect undocumented items
        doc_items = []
        
        # Process functions
        for func in file_data.get('functions', []):
            if not func.get('docstring'):
                docstring = self.python_writer.generate_function_doc(func, file_content)
                doc_items.append(DocItem(
                    type='function',
                    name=func['name'],
                    line_start=func['line_start'],
                    docstring=docstring
                ))
        
        # Process classes and methods
        for cls in file_data.get('classes', []):
            if not cls.get('docstring'):
                docstring = self.python_writer.generate_class_doc(cls, file_content)
                doc_items.append(DocItem(
                    type='class',
                    name=cls['name'],
                    line_start=cls['line_start'],
                    docstring=docstring
                ))
            
            for method in cls.get('methods', []):
                if not method.get('docstring'):
                    docstring = self.python_writer.generate_method_doc(
                        method, cls['name'], file_content
                    )
                    doc_items.append(DocItem(
                        type='method',
                        name=f"{cls['name']}.{method['name']}",
                        line_start=method['line_start'],
                        docstring=docstring
                    ))
        
        # Insert documentation
        if not self.dry_run and doc_items:
            result = self.inserter.insert_documentation(
                file_path, 
                doc_items,
                create_backup=self.create_backup
            )
            return FileReport(
                file_path=str(file_path),
                items_documented=len(doc_items),
                success=result.success
            )
        else:
            return FileReport(
                file_path=str(file_path),
                items_documented=len(doc_items),
                success=True,
                dry_run=True
            )
```

### 7. CLI Integration

**File: `scanner.py` (modifications)**

**New Arguments**:
```python
parser.add_argument(
    '--write-docs',
    action='store_true',
    help='Generate and insert documentation for undocumented Python items'
)

parser.add_argument(
    '--dry-run',
    action='store_true',
    help='Show what would be documented without modifying files'
)

parser.add_argument(
    '--no-backup',
    action='store_true',
    help='Skip creating backup files (not recommended)'
)

parser.add_argument(
    '--min-coverage',
    type=float,
    default=80.0,
    help='Target minimum documentation coverage percentage (default: 80.0)'
)
```

**Modified main() function**:
```python
def main():
    # ... existing argument parsing ...
    
    # Run initial scan
    scan_codebase(config, output_format=args.format)
    
    # If --write-docs flag is set
    if args.write_docs:
        logger.info("=" * 60)
        logger.info("DOCUMENTATION GENERATION MODE")
        logger.info("=" * 60)
        
        # Check environment variables
        if not all([
            os.getenv('WATSONX_API_KEY'),
            os.getenv('WATSONX_PROJECT_ID'),
            os.getenv('WATSONX_URL')
        ]):
            print("\nError: watsonx.ai credentials not found!")
            print("Please set the following environment variables:")
            print("  - WATSONX_API_KEY")
            print("  - WATSONX_PROJECT_ID")
            print("  - WATSONX_URL")
            print("\nSee .env.example for details.")
            sys.exit(1)
        
        # Load scan results
        output_path = Path(config.get('output_file', 'output/documentation.json'))
        with open(output_path, 'r') as f:
            scan_data = json.load(f)
        
        # Initialize watsonx client
        watsonx_client = WatsonxClient(
            api_key=os.getenv('WATSONX_API_KEY'),
            project_id=os.getenv('WATSONX_PROJECT_ID'),
            url=os.getenv('WATSONX_URL')
        )
        
        # Generate documentation
        generator = DocumentationGenerator(
            logger=logger,
            watsonx_client=watsonx_client,
            dry_run=args.dry_run,
            create_backup=not args.no_backup,
            min_coverage=args.min_coverage
        )
        
        initial_coverage = scan_data['coverage_report']['overall_coverage']
        logger.info(f"Initial documentation coverage: {initial_coverage:.1f}%")
        
        report = generator.generate_documentation(scan_data, config)
        
        # Re-scan to verify improvements
        if not args.dry_run:
            logger.info("Re-scanning to verify coverage improvements...")
            scan_codebase(config, output_format=args.format)
            
            with open(output_path, 'r') as f:
                updated_data = json.load(f)
            
            final_coverage = updated_data['coverage_report']['overall_coverage']
            
            # Display results
            logger.info("=" * 60)
            logger.info("DOCUMENTATION GENERATION COMPLETE")
            logger.info("=" * 60)
            logger.info(f"Files modified: {report.files_modified}")
            logger.info(f"Items documented: {report.items_documented}")
            logger.info(f"Coverage before: {initial_coverage:.1f}%")
            logger.info(f"Coverage after: {final_coverage:.1f}%")
            logger.info(f"Improvement: +{final_coverage - initial_coverage:.1f}%")
        else:
            logger.info("=" * 60)
            logger.info("DRY RUN COMPLETE (no files modified)")
            logger.info("=" * 60)
            logger.info(f"Would document {report.items_documented} items in {report.files_modified} files")
```

## Data Structures

```python
@dataclass
class DocItem:
    """Represents a documentation item to be inserted"""
    type: str  # 'function', 'method', 'class'
    name: str
    line_start: int
    docstring: str

@dataclass
class FileReport:
    """Report for a single file"""
    file_path: str
    items_documented: int
    success: bool
    dry_run: bool = False
    error: Optional[str] = None

@dataclass
class GenerationReport:
    """Overall generation report"""
    files_modified: int = 0
    items_documented: int = 0
    file_reports: List[FileReport] = field(default_factory=list)
    
    def add_file_report(self, report: FileReport):
        self.file_reports.append(report)
        if report.success:
            self.files_modified += 1
            self.items_documented += report.items_documented
```

## Implementation Steps

### Step 1: Setup Environment
- [x] Create `.env.example` file
- [ ] Update `.gitignore` to exclude `.env`
- [ ] Create `writers/` directory

### Step 2: Implement watsonx.ai Client
- [ ] Create `writers/watsonx_client.py`
- [ ] Implement credential loading from environment
- [ ] Implement API request/response handling
- [ ] Add error handling and retry logic
- [ ] Test API connectivity

### Step 3: Implement Base Writer
- [ ] Create `writers/base_writer.py`
- [ ] Define abstract interface
- [ ] Implement validation methods
- [ ] Add utility methods

### Step 4: Implement Python Writer
- [ ] Create `writers/python_writer.py`
- [ ] Implement function docstring generation
- [ ] Implement class docstring generation
- [ ] Implement method docstring generation
- [ ] Add prompt engineering for watsonx.ai
- [ ] Test with sample functions

### Step 5: Implement Documentation Inserter
- [ ] Create `writers/doc_inserter.py`
- [ ] Implement backup creation
- [ ] Implement safe insertion logic
- [ ] Implement syntax validation
- [ ] Implement rollback mechanism
- [ ] Test with sample files

### Step 6: Implement Documentation Generator
- [ ] Create `core/doc_generator.py`
- [ ] Implement orchestration logic
- [ ] Implement file filtering
- [ ] Implement progress reporting
- [ ] Test end-to-end workflow

### Step 7: Integrate with Scanner
- [ ] Add CLI arguments to `scanner.py`
- [ ] Add environment variable checks
- [ ] Integrate documentation generation workflow
- [ ] Add before/after comparison
- [ ] Test complete workflow

### Step 8: Testing
- [ ] Create unit tests for watsonx client
- [ ] Create unit tests for Python writer
- [ ] Create unit tests for doc inserter
- [ ] Create integration tests
- [ ] Test with demo/ directory files

## Usage Examples

### Basic Usage
```bash
# Set environment variables
export WATSONX_API_KEY="your_key"
export WATSONX_PROJECT_ID="your_project_id"
export WATSONX_URL="https://us-south.ml.cloud.ibm.com"

# Scan and generate documentation
python scanner.py --write-docs

# Preview without modifying files
python scanner.py --write-docs --dry-run

# Target specific directory
python scanner.py --root ./demo --write-docs
```

### Expected Output
```
Starting codebase scan...
Root directory: /path/to/project
...
Scan complete! Results saved to: output/documentation.json

============================================================
DOCUMENTATION GENERATION MODE
============================================================
Initial documentation coverage: 45.2%
Generating documentation for undocumented items...

Processing demo/utils.py...
  ✓ Documented 5 functions
Processing demo/data_processor.py...
  ✓ Documented 8 functions
...

Re-scanning to verify coverage improvements...

============================================================
DOCUMENTATION GENERATION COMPLETE
============================================================
Files modified: 3
Items documented: 15
Coverage before: 45.2%
Coverage after: 87.8%
Improvement: +42.6%
```

## Error Handling

### Missing Credentials
```
Error: watsonx.ai credentials not found!
Please set the following environment variables:
  - WATSONX_API_KEY
  - WATSONX_PROJECT_ID
  - WATSONX_URL

See .env.example for details.
```

### API Errors
- Rate limiting: Implement exponential backoff
- Network errors: Retry up to 3 times
- Invalid responses: Log error and skip item
- Authentication errors: Exit with clear message

### File Errors
- Syntax errors after insertion: Restore from backup
- Permission errors: Skip file and log warning
- Encoding errors: Try alternative encodings

## Success Criteria

- ✓ Generate Google-style docstrings for Python functions, methods, and classes
- ✓ Use watsonx.ai granite-3-8b-instruct model for generation
- ✓ Insert documentation without breaking code syntax
- ✓ Create backups before modification
- ✓ Calculate and report coverage improvements
- ✓ Handle errors gracefully with rollback
- ✓ No placeholder text in generated documentation
- ✓ Clear error messages for missing credentials

## Next Steps

1. Review this plan and approve
2. Switch to Code mode to begin implementation
3. Start with Step 1 (Setup Environment)
4. Proceed sequentially through implementation steps
5. Test thoroughly with demo/ directory files