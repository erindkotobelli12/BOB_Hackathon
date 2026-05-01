# Quick Start Guide: Implementing --write-docs Feature

## Overview
This guide provides a step-by-step walkthrough for implementing the `--write-docs` feature. Follow these steps in order for a smooth implementation.

## Prerequisites
- Python 3.8+
- Existing codebase scanner is functional
- All dependencies installed (`pip install -r requirements.txt`)

## Implementation Steps

### Step 1: Create Directory Structure (5 minutes)

```bash
cd codebase-scanner
mkdir -p writers
touch writers/__init__.py
touch writers/base_writer.py
touch writers/python_writer.py
touch writers/javascript_writer.py
touch writers/java_writer.py
touch writers/cpp_writer.py
touch writers/doc_inserter.py
```

### Step 2: Implement Base Writer (1 hour)

**File**: [`writers/base_writer.py`](codebase-scanner/writers/base_writer.py)

**Key Components**:
1. Abstract base class with `@abstractmethod` decorators
2. Parameter inference logic
3. Documentation validation (no placeholders)
4. Common utility methods

**Reference**: See [TECHNICAL_SPECIFICATION.md](codebase-scanner/TECHNICAL_SPECIFICATION.md) Section 2.1

**Test**: Create `tests/test_base_writer.py` and verify interface

### Step 3: Implement Documentation Inserter (2 hours)

**File**: [`writers/doc_inserter.py`](codebase-scanner/writers/doc_inserter.py)

**Key Features**:
1. Backup creation (`.bak` files)
2. Safe file modification (atomic operations)
3. Syntax validation
4. Automatic rollback on errors

**Critical Safety Checks**:
```python
# Always create backup first
backup_path = self._create_backup(file_path)

# Write to temp file, not directly
temp_fd, temp_path = tempfile.mkstemp()

# Validate before committing
if self._validate_syntax(temp_path, language):
    shutil.move(temp_path, file_path)
else:
    shutil.copy2(backup_path, file_path)
```

**Test**: Create `tests/test_doc_inserter.py` with backup/restore scenarios

### Step 4: Implement Python Writer (3 hours)

**File**: [`writers/python_writer.py`](codebase-scanner/writers/python_writer.py)

**Implementation Checklist**:
- [ ] Google-style docstring format
- [ ] Parameter inference from names/types
- [ ] Brief description generation
- [ ] Args section with types
- [ ] Returns section
- [ ] Handle `*args` and `**kwargs`
- [ ] Support async functions

**Example Test Case**:
```python
def test_generate_function_doc():
    writer = PythonDocumentationWriter()
    func_info = {
        'name': 'calculate_sum',
        'parameters': [
            {'name': 'numbers', 'type': 'List[int]', 'default': None},
            {'name': 'verbose', 'type': 'bool', 'default': 'False'}
        ],
        'return_type': 'int',
        'indentation': 4
    }
    doc = writer.generate_function_doc(func_info)
    assert '"""' in doc
    assert 'Args:' in doc
    assert 'Returns:' in doc
    assert 'numbers (List[int]):' in doc
```

**Test**: Create `tests/test_python_writer.py` with 10+ test cases

### Step 5: Implement JavaScript Writer (2 hours)

**File**: [`writers/javascript_writer.py`](codebase-scanner/writers/javascript_writer.py)

**JSDoc Format**:
```javascript
/**
 * Brief description
 * @param {type} name - Description
 * @returns {type} Description
 * @async
 */
```

**Test**: Create `tests/test_javascript_writer.py`

### Step 6: Implement Java Writer (2 hours)

**File**: [`writers/java_writer.py`](codebase-scanner/writers/java_writer.py)

**Javadoc Format**:
```java
/**
 * Brief description.
 *
 * @param name Description
 * @return Description
 * @throws Exception Description
 */
```

**Test**: Create `tests/test_java_writer.py`

### Step 7: Implement C++ Writer (2 hours)

**File**: [`writers/cpp_writer.py`](codebase-scanner/writers/cpp_writer.py)

**Doxygen Format**:
```cpp
/**
 * @brief Brief description
 * @param name Description
 * @return Description
 */
```

**Test**: Create `tests/test_cpp_writer.py`

### Step 8: Create Documentation Generator (3 hours)

**File**: [`core/doc_generator.py`](codebase-scanner/core/doc_generator.py)

**Key Responsibilities**:
1. Load scan results from JSON
2. Filter undocumented items
3. Get appropriate writer for each language
4. Orchestrate documentation generation
5. Calculate coverage improvements
6. Generate reports

**Main Method Structure**:
```python
def generate_documentation(self, scan_data: Dict, config: Dict) -> GenerationReport:
    # 1. Extract undocumented items
    undocumented = self._filter_undocumented(scan_data)
    
    # 2. Group by file and language
    by_file = self._group_by_file(undocumented)
    
    # 3. Process each file
    for file_path, items in by_file.items():
        language = self._detect_language(file_path)
        writer = self._get_writer(language)
        
        # Generate docs
        docs = [writer.generate_function_doc(item) for item in items]
        
        # Insert into file
        success = self.inserter.insert_documentation(file_path, docs, language)
        
        # Track results
        self._record_result(file_path, success)
    
    # 4. Generate report
    return self._create_report()
```

**Test**: Create `tests/test_doc_generator.py`

### Step 9: Modify scanner.py (2 hours)

**File**: [`scanner.py`](codebase-scanner/scanner.py)

**Changes Required**:

1. **Add CLI Arguments** (after line 190):
```python
parser.add_argument(
    '--write-docs',
    action='store_true',
    help='Automatically generate and insert documentation'
)

parser.add_argument(
    '--dry-run',
    action='store_true',
    help='Preview documentation without modifying files'
)

parser.add_argument(
    '--min-coverage',
    type=float,
    default=80.0,
    help='Target minimum documentation coverage (default: 80.0)'
)
```

2. **Add Documentation Generation Logic** (after line 271):
```python
if args.write_docs:
    from core.doc_generator import DocumentationGenerator
    
    logger.info("=" * 60)
    logger.info("DOCUMENTATION GENERATION MODE")
    logger.info("=" * 60)
    
    # Load scan results
    output_path = Path(config.get('output_file'))
    with open(output_path, 'r') as f:
        scan_data = json.load(f)
    
    # Generate documentation
    generator = DocumentationGenerator(
        logger=logger,
        dry_run=args.dry_run,
        min_coverage=args.min_coverage
    )
    
    report = generator.generate_documentation(scan_data, config)
    
    # Display results
    logger.info(f"Files modified: {report.total_files_modified}")
    logger.info(f"Items documented: {report.total_items_documented}")
    logger.info(f"Coverage improvement: +{report.coverage_improvement:.2f}%")
```

### Step 10: Integration Testing (2 hours)

**Create Test Project**:
```bash
mkdir -p test_project/src
```

**Create Sample Files**:

`test_project/src/utils.py`:
```python
def calculate_total(items):
    return sum(items)

def format_name(first, last):
    return f"{first} {last}"
```

`test_project/src/api.js`:
```javascript
function fetchData(url, options) {
    return fetch(url, options);
}
```

**Run Test**:
```bash
# Scan test project
python scanner.py --root test_project --write-docs --dry-run

# Verify output shows what would be documented

# Actually generate docs
python scanner.py --root test_project --write-docs

# Verify files are documented correctly
cat test_project/src/utils.py
```

### Step 11: Run Full Test Suite (1 hour)

```bash
# Run all unit tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=writers --cov=core --cov-report=html

# Check coverage report
open htmlcov/index.html
```

**Target Coverage**: 90%+ for new code

### Step 12: Update Documentation (1 hour)

**Update README.md**:
Add section after existing usage examples:

```markdown
## Automatic Documentation Generation

The scanner can automatically generate and insert documentation for undocumented code:

### Basic Usage
\`\`\`bash
# Generate documentation for all undocumented items
python scanner.py --write-docs

# Preview without modifying files
python scanner.py --write-docs --dry-run

# Target specific coverage threshold
python scanner.py --write-docs --min-coverage 90
\`\`\`

### Supported Languages
- **Python**: Google-style docstrings
- **JavaScript/TypeScript**: JSDoc comments
- **Java**: Javadoc comments
- **C/C++**: Doxygen comments

### Safety Features
- Automatic backup creation (`.bak` files)
- Syntax validation before committing changes
- Automatic rollback on errors
- Atomic file operations

### Example Output
\`\`\`
Files modified: 12
Items documented: 156
Coverage before: 45.2%
Coverage after: 87.8%
Improvement: +42.6%
\`\`\`
```

## Verification Checklist

Before considering implementation complete:

- [ ] All unit tests pass
- [ ] Integration tests pass with sample projects
- [ ] Test coverage ≥ 90% for new code
- [ ] No placeholder text in generated documentation
- [ ] Backup/restore mechanism works correctly
- [ ] Syntax validation prevents broken code
- [ ] All four languages (Python, JS, Java, C++) supported
- [ ] CLI help text is clear and accurate
- [ ] README updated with usage examples
- [ ] Error messages are helpful and actionable

## Common Issues & Solutions

### Issue: Syntax errors after documentation insertion
**Solution**: Check indentation detection logic in `doc_inserter.py`. Ensure documentation matches surrounding code indentation exactly.

### Issue: Generated docs contain placeholder text
**Solution**: Review parameter inference logic in language-specific writers. Add more patterns to `infer_parameter_description()`.

### Issue: Backup files not being created
**Solution**: Check file permissions and disk space. Verify `create_backup` flag is set to `True`.

### Issue: Coverage not improving after generation
**Solution**: Verify re-scan is happening after documentation insertion. Check that parsers recognize the new documentation format.

## Performance Optimization Tips

1. **Batch Processing**: Process files in batches of 10-20 for better memory usage
2. **Parallel Processing**: Use `multiprocessing` for large codebases (100+ files)
3. **Caching**: Cache parsed ASTs to avoid re-parsing
4. **Skip Large Files**: Add `max_file_size_mb` check before processing

## Next Steps After Implementation

1. **Beta Testing**: Test with real-world projects
2. **User Feedback**: Gather feedback on documentation quality
3. **Refinement**: Improve parameter inference based on feedback
4. **Additional Languages**: Add support for Go, Rust, PHP, etc.
5. **IDE Integration**: Create VS Code extension for inline documentation

## Support & Resources

- **Implementation Plan**: [WRITE_DOCS_IMPLEMENTATION_PLAN.md](WRITE_DOCS_IMPLEMENTATION_PLAN.md)
- **Technical Spec**: [TECHNICAL_SPECIFICATION.md](TECHNICAL_SPECIFICATION.md)
- **Architecture**: [ARCHITECTURE_DIAGRAM.md](ARCHITECTURE_DIAGRAM.md)
- **Summary**: [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)

## Estimated Timeline

| Step | Duration | Cumulative |
|------|----------|------------|
| 1-2  | 1 hour   | 1 hour     |
| 3    | 2 hours  | 3 hours    |
| 4    | 3 hours  | 6 hours    |
| 5-7  | 6 hours  | 12 hours   |
| 8    | 3 hours  | 15 hours   |
| 9    | 2 hours  | 17 hours   |
| 10   | 2 hours  | 19 hours   |
| 11   | 1 hour   | 20 hours   |
| 12   | 1 hour   | 21 hours   |

**Total**: ~21 hours (approximately 3 working days)

## Ready to Start?

Begin with Step 1 and work through sequentially. Each step builds on the previous one, so don't skip ahead. Good luck! 🚀