# Technical Specification: Documentation Writer System

## 1. Data Structures

### 1.1 DocItem
Represents a single item that needs documentation.

```python
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class DocItem:
    """Represents an item requiring documentation."""
    file_path: str
    item_type: str  # 'function', 'method', 'class'
    name: str
    line_number: int
    parameters: List[Dict[str, Any]]
    return_type: Optional[str]
    is_async: bool
    decorators: List[str]
    class_name: Optional[str]  # For methods
    indentation: int  # Number of spaces for indentation
    existing_doc: Optional[str]  # Existing partial documentation
```

### 1.2 GenerationReport
Report of documentation generation results.

```python
@dataclass
class FileReport:
    """Report for a single file."""
    file_path: str
    language: str
    coverage_before: float
    coverage_after: float
    items_documented: int
    success: bool
    error_message: Optional[str]
    backup_path: Optional[str]

@dataclass
class GenerationReport:
    """Overall documentation generation report."""
    total_files_processed: int
    total_files_modified: int
    total_items_documented: int
    overall_coverage_before: float
    overall_coverage_after: float
    file_reports: List[FileReport]
    errors: List[Dict[str, str]]
    duration_seconds: float
```

## 2. Base Writer API

### 2.1 BaseDocumentationWriter

```python
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

class BaseDocumentationWriter(ABC):
    """Abstract base class for language-specific documentation writers."""
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize documentation writer.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.placeholder_patterns = [
            'TODO', 'FIXME', 'XXX', 'HACK',
            'Description here', 'Fill this in',
            'Add description', 'Your description'
        ]
    
    @abstractmethod
    def get_doc_start_marker(self) -> str:
        """Return language-specific documentation start marker."""
        pass
    
    @abstractmethod
    def get_doc_end_marker(self) -> str:
        """Return language-specific documentation end marker."""
        pass
    
    @abstractmethod
    def format_doc_line(self, line: str, indentation: int = 0) -> str:
        """Format a single line of documentation with proper indentation."""
        pass
    
    def generate_function_doc(self, func_info: Dict) -> str:
        """
        Generate documentation for a function.
        
        Args:
            func_info: Dictionary containing function metadata
                - name: Function name
                - parameters: List of parameter dictionaries
                - return_type: Return type annotation
                - is_async: Whether function is async
                - decorators: List of decorators
        
        Returns:
            Generated documentation string
        """
        pass
    
    def generate_method_doc(self, method_info: Dict, class_name: str) -> str:
        """
        Generate documentation for a class method.
        
        Args:
            method_info: Dictionary containing method metadata
            class_name: Name of the containing class
        
        Returns:
            Generated documentation string
        """
        pass
    
    def generate_class_doc(self, class_info: Dict) -> str:
        """
        Generate documentation for a class.
        
        Args:
            class_info: Dictionary containing class metadata
                - name: Class name
                - base_classes: List of base class names
                - methods: List of method dictionaries
        
        Returns:
            Generated documentation string
        """
        pass
    
    def infer_parameter_description(self, param_name: str, param_type: Optional[str]) -> str:
        """
        Infer parameter description from name and type.
        
        Args:
            param_name: Parameter name
            param_type: Parameter type annotation (if available)
        
        Returns:
            Inferred description string
        """
        # Common parameter name patterns
        patterns = {
            r'.*path$': 'Path to file or directory',
            r'.*file.*': 'File to process',
            r'.*dir.*': 'Directory path',
            r'.*name$': 'Name of the entity',
            r'.*config$': 'Configuration dictionary',
            r'.*options$': 'Options dictionary',
            r'.*data$': 'Data to process',
            r'.*content$': 'Content to process',
            r'.*logger$': 'Logger instance',
            r'.*verbose$': 'Enable verbose output',
            r'^is_.*': 'Whether to perform action',
            r'^has_.*': 'Whether entity has property',
            r'^should_.*': 'Whether should perform action',
            r'^enable.*': 'Enable specific feature',
            r'^disable.*': 'Disable specific feature',
        }
        
        # Type-based inference
        if param_type:
            if 'bool' in param_type.lower():
                return f'Boolean flag for {param_name}'
            elif 'list' in param_type.lower():
                return f'List of items'
            elif 'dict' in param_type.lower():
                return f'Dictionary containing data'
        
        # Name-based inference
        import re
        for pattern, description in patterns.items():
            if re.match(pattern, param_name, re.IGNORECASE):
                return description
        
        # Default fallback
        return f'{param_name.replace("_", " ").capitalize()}'
    
    def validate_documentation(self, doc: str) -> bool:
        """
        Validate that documentation doesn't contain placeholders.
        
        Args:
            doc: Documentation string to validate
        
        Returns:
            True if valid, False if contains placeholders
        """
        doc_lower = doc.lower()
        for pattern in self.placeholder_patterns:
            if pattern.lower() in doc_lower:
                return False
        return True
    
    def format_parameter(self, param: Dict) -> str:
        """
        Format a parameter for documentation.
        
        Args:
            param: Parameter dictionary with 'name', 'type', 'default'
        
        Returns:
            Formatted parameter string
        """
        pass
```

## 3. Python Writer Implementation

### 3.1 PythonDocumentationWriter

```python
class PythonDocumentationWriter(BaseDocumentationWriter):
    """Generate Google-style Python docstrings."""
    
    def get_doc_start_marker(self) -> str:
        return '"""'
    
    def get_doc_end_marker(self) -> str:
        return '"""'
    
    def format_doc_line(self, line: str, indentation: int = 0) -> str:
        """Format line with proper indentation."""
        indent = ' ' * indentation
        return f'{indent}{line}'
    
    def generate_function_doc(self, func_info: Dict) -> str:
        """Generate Google-style docstring for function."""
        lines = []
        indent = func_info.get('indentation', 4)
        
        # Start marker
        lines.append(self.format_doc_line('"""', indent))
        
        # Brief description
        brief = self._generate_brief_description(func_info['name'])
        lines.append(self.format_doc_line(brief, indent))
        
        # Parameters section
        params = func_info.get('parameters', [])
        if params:
            lines.append(self.format_doc_line('', indent))
            lines.append(self.format_doc_line('Args:', indent))
            
            for param in params:
                param_doc = self._format_python_parameter(param)
                lines.append(self.format_doc_line(f'    {param_doc}', indent))
        
        # Returns section
        return_type = func_info.get('return_type')
        if return_type and return_type != 'None':
            lines.append(self.format_doc_line('', indent))
            lines.append(self.format_doc_line('Returns:', indent))
            return_desc = self._infer_return_description(func_info['name'], return_type)
            lines.append(self.format_doc_line(f'    {return_type}: {return_desc}', indent))
        
        # End marker
        lines.append(self.format_doc_line('"""', indent))
        
        return '\n'.join(lines)
    
    def _format_python_parameter(self, param: Dict) -> str:
        """Format parameter in Google style."""
        name = param['name']
        param_type = param.get('type', 'Any')
        default = param.get('default')
        
        # Infer description
        description = self.infer_parameter_description(name, param_type)
        
        # Format with optional marker
        if default is not None:
            return f'{name} ({param_type}, optional): {description}. Defaults to {default}.'
        else:
            return f'{name} ({param_type}): {description}'
    
    def _generate_brief_description(self, name: str) -> str:
        """Generate brief description from function name."""
        # Convert snake_case to words
        words = name.replace('_', ' ').split()
        
        # Common verb patterns
        if words[0] in ['get', 'fetch', 'retrieve']:
            return f'Retrieve {" ".join(words[1:])}.'
        elif words[0] in ['set', 'update', 'modify']:
            return f'Update {" ".join(words[1:])}.'
        elif words[0] in ['create', 'make', 'build']:
            return f'Create {" ".join(words[1:])}.'
        elif words[0] in ['delete', 'remove']:
            return f'Delete {" ".join(words[1:])}.'
        elif words[0] in ['check', 'verify', 'validate']:
            return f'Verify {" ".join(words[1:])}.'
        elif words[0] in ['is', 'has']:
            return f'Check if {" ".join(words[1:])}.'
        elif words[0] == 'calculate':
            return f'Calculate {" ".join(words[1:])}.'
        elif words[0] == 'parse':
            return f'Parse {" ".join(words[1:])}.'
        elif words[0] == 'format':
            return f'Format {" ".join(words[1:])}.'
        else:
            return f'{name.replace("_", " ").capitalize()}.'
    
    def _infer_return_description(self, func_name: str, return_type: str) -> str:
        """Infer return value description."""
        if 'bool' in return_type.lower():
            return 'True if successful, False otherwise'
        elif 'list' in return_type.lower():
            return 'List of results'
        elif 'dict' in return_type.lower():
            return 'Dictionary containing results'
        elif 'str' in return_type.lower():
            return 'String result'
        elif 'int' in return_type.lower() or 'float' in return_type.lower():
            return 'Numeric result'
        else:
            return 'Result of operation'
```

## 4. Documentation Inserter

### 4.1 DocumentationInserter

```python
import shutil
from pathlib import Path
from typing import List, Optional, Tuple
import tempfile

class DocumentationInserter:
    """Safely insert documentation into source files."""
    
    def __init__(self, create_backup: bool = True, validate_syntax: bool = True):
        """
        Initialize documentation inserter.
        
        Args:
            create_backup: Whether to create backup files
            validate_syntax: Whether to validate syntax after insertion
        """
        self.create_backup = create_backup
        self.validate_syntax = validate_syntax
    
    def insert_documentation(
        self,
        file_path: Path,
        doc_items: List[Tuple[int, str]],
        language: str
    ) -> Tuple[bool, Optional[str]]:
        """
        Insert documentation into file.
        
        Args:
            file_path: Path to source file
            doc_items: List of (line_number, documentation) tuples
            language: Programming language
        
        Returns:
            Tuple of (success, error_message)
        """
        backup_path = None
        
        try:
            # Create backup
            if self.create_backup:
                backup_path = self._create_backup(file_path)
            
            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Sort items by line number (descending) to maintain line numbers
            sorted_items = sorted(doc_items, key=lambda x: x[0], reverse=True)
            
            # Insert documentation
            for line_num, doc in sorted_items:
                # Insert before the specified line (0-based index)
                insert_index = line_num - 1
                doc_lines = doc.split('\n')
                
                # Add newline to each doc line if not present
                doc_lines = [line if line.endswith('\n') else line + '\n' 
                            for line in doc_lines]
                
                # Insert documentation
                lines[insert_index:insert_index] = doc_lines
            
            # Write to temporary file
            temp_fd, temp_path = tempfile.mkstemp(suffix=file_path.suffix)
            try:
                with os.fdopen(temp_fd, 'w', encoding='utf-8') as f:
                    f.writelines(lines)
                
                # Validate syntax if required
                if self.validate_syntax:
                    if not self._validate_syntax(Path(temp_path), language):
                        raise SyntaxError('Generated documentation breaks syntax')
                
                # Atomic replace
                shutil.move(temp_path, file_path)
                
                return True, None
                
            finally:
                # Clean up temp file if it still exists
                if Path(temp_path).exists():
                    Path(temp_path).unlink()
        
        except Exception as e:
            # Restore from backup on error
            if backup_path and Path(backup_path).exists():
                shutil.copy2(backup_path, file_path)
            
            return False, str(e)
    
    def _create_backup(self, file_path: Path) -> Path:
        """Create backup file."""
        backup_path = file_path.with_suffix(file_path.suffix + '.bak')
        shutil.copy2(file_path, backup_path)
        return backup_path
    
    def _validate_syntax(self, file_path: Path, language: str) -> bool:
        """Validate file syntax after modification."""
        if language == 'python':
            return self._validate_python_syntax(file_path)
        elif language in ['javascript', 'typescript']:
            return self._validate_javascript_syntax(file_path)
        # Add other language validators as needed
        return True
    
    def _validate_python_syntax(self, file_path: Path) -> bool:
        """Validate Python syntax."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                compile(f.read(), str(file_path), 'exec')
            return True
        except SyntaxError:
            return False
```

## 5. Integration Points

### 5.1 Modified scanner.py main() function

```python
def main():
    # ... existing argument parsing ...
    
    # Run initial scan
    logger.info("Starting initial codebase scan...")
    scan_codebase(config, output_format=args.format)
    
    # If --write-docs flag is set
    if args.write_docs:
        logger.info("=" * 60)
        logger.info("DOCUMENTATION GENERATION MODE")
        logger.info("=" * 60)
        
        # Load scan results
        output_path = Path(config.get('output_file', 'output/documentation.json'))
        
        if not output_path.exists():
            logger.error(f"Scan output not found: {output_path}")
            sys.exit(1)
        
        with open(output_path, 'r', encoding='utf-8') as f:
            scan_data = json.load(f)
        
        # Store initial coverage
        initial_coverage = scan_data['coverage_report']['overall_coverage']
        logger.info(f"Initial documentation coverage: {initial_coverage:.2f}%")
        
        # Generate documentation
        from core.doc_generator import DocumentationGenerator
        
        generator = DocumentationGenerator(
            logger=logger,
            dry_run=args.dry_run,
            create_backup=args.backup,
            min_coverage=args.min_coverage
        )
        
        logger.info("Generating documentation for undocumented items...")
        report = generator.generate_documentation(scan_data, config)
        
        if not args.dry_run:
            # Re-scan to verify improvements
            logger.info("Re-scanning to verify coverage improvements...")
            scan_codebase(config, output_format=args.format)
            
            # Load updated results
            with open(output_path, 'r', encoding='utf-8') as f:
                updated_data = json.load(f)
            
            final_coverage = updated_data['coverage_report']['overall_coverage']
            improvement = final_coverage - initial_coverage
            
            # Display results
            logger.info("=" * 60)
            logger.info("DOCUMENTATION GENERATION COMPLETE")
            logger.info("=" * 60)
            logger.info(f"Files modified: {report.total_files_modified}")
            logger.info(f"Items documented: {report.total_items_documented}")
            logger.info(f"Coverage before: {initial_coverage:.2f}%")
            logger.info(f"Coverage after: {final_coverage:.2f}%")
            logger.info(f"Improvement: +{improvement:.2f}%")
            
            if report.errors:
                logger.warning(f"Errors encountered: {len(report.errors)}")
                for error in report.errors[:5]:  # Show first 5 errors
                    logger.warning(f"  - {error['file']}: {error['message']}")
        else:
            logger.info("DRY RUN - No files were modified")
            logger.info(f"Would document {report.total_items_documented} items in {report.total_files_modified} files")
```

## 6. Configuration Options

### 6.1 Extended config.json

```json
{
  "root_directory": ".",
  "output_file": "output/documentation.json",
  "exclude_patterns": ["node_modules/**", "venv/**"],
  "include_extensions": [".py", ".js", ".ts", ".java", ".cpp"],
  
  "documentation_generation": {
    "enabled": false,
    "create_backup": true,
    "validate_syntax": true,
    "min_coverage_target": 80.0,
    "dry_run": false,
    
    "python": {
      "style": "google",
      "include_type_hints": true,
      "infer_exceptions": true
    },
    
    "javascript": {
      "style": "jsdoc",
      "include_types": true,
      "mark_async": true
    },
    
    "java": {
      "style": "javadoc",
      "include_since_tag": true,
      "version": "1.0"
    },
    
    "cpp": {
      "style": "doxygen",
      "comment_style": "/**",
      "include_brief": true
    }
  }
}
```

## 7. Error Codes

```python
class DocGenerationError(Exception):
    """Base exception for documentation generation errors."""
    pass

class SyntaxValidationError(DocGenerationError):
    """Raised when generated documentation breaks syntax."""
    pass

class FileAccessError(DocGenerationError):
    """Raised when file cannot be accessed."""
    pass

class BackupError(DocGenerationError):
    """Raised when backup creation fails."""
    pass
```

## 8. Performance Considerations

- **Batch Processing**: Process files in batches to manage memory
- **Parallel Processing**: Use multiprocessing for large codebases
- **Caching**: Cache parsed ASTs to avoid re-parsing
- **Incremental Updates**: Only process files that changed since last scan

## 9. Security Considerations

- **Path Traversal**: Validate all file paths are within project directory
- **Code Injection**: Never execute generated code, only parse
- **File Permissions**: Preserve original file permissions
- **Backup Integrity**: Verify backup before deletion