# Implementation Plan: --write-docs Feature

## Overview
Add a `--write-docs` flag to the codebase scanner that automatically generates and inserts language-specific documentation for undocumented functions, methods, and classes. The system will support Python (Google-style), JavaScript/TypeScript (JSDoc), Java (Javadoc), and C/C++ (Doxygen) formats.

## Architecture Design

### 1. Module Structure
```
codebase-scanner/
├── writers/                          # NEW: Documentation writers
│   ├── __init__.py
│   ├── base_writer.py               # Abstract base class
│   ├── python_writer.py             # Google-style docstrings
│   ├── javascript_writer.py         # JSDoc comments
│   ├── java_writer.py               # Javadoc comments
│   ├── cpp_writer.py                # Doxygen comments
│   └── doc_inserter.py              # File modification engine
├── core/
│   └── doc_generator.py             # NEW: Orchestrates documentation generation
└── scanner.py                        # MODIFY: Add --write-docs flag
```

### 2. Component Responsibilities

#### 2.1 BaseDocumentationWriter (writers/base_writer.py)
**Purpose**: Abstract base class defining the interface for all language-specific writers

**Key Methods**:
- `generate_function_doc(func_info: Dict) -> str`: Generate documentation for a function
- `generate_method_doc(method_info: Dict, class_name: str) -> str`: Generate documentation for a method
- `generate_class_doc(class_info: Dict) -> str`: Generate documentation for a class
- `format_parameter(param: Dict) -> str`: Format a single parameter description
- `infer_parameter_description(param_name: str, param_type: str) -> str`: Infer parameter purpose from name/type
- `validate_documentation(doc: str) -> bool`: Ensure no placeholder text exists

**Abstract Methods** (must be implemented by subclasses):
- `get_doc_start_marker() -> str`: Return language-specific doc start (e.g., '"""', '/**')
- `get_doc_end_marker() -> str`: Return language-specific doc end
- `format_doc_line(line: str) -> str`: Format a single line of documentation

#### 2.2 PythonDocumentationWriter (writers/python_writer.py)
**Purpose**: Generate Google-style Python docstrings

**Documentation Format**:
```python
"""Brief description of function purpose.

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

**Key Features**:
- Extract parameter names and types from function signature
- Infer parameter descriptions from naming conventions (e.g., `file_path` → "Path to file")
- Handle `*args` and `**kwargs` appropriately
- Include return type from type hints
- Detect common exception patterns (try/except blocks)
- Support async functions with appropriate notation

**Parameter Inference Rules**:
- `path`, `file_path`, `dir_path` → "Path to [file/directory]"
- `name`, `filename` → "Name of [entity]"
- `data`, `content` → "Data/content to process"
- `config`, `options` → "Configuration/options dictionary"
- `logger` → "Logger instance"
- `verbose` → "Enable verbose output"
- Boolean params → "Whether to [action]"

#### 2.3 JavaScriptDocumentationWriter (writers/javascript_writer.py)
**Purpose**: Generate JSDoc comments for JavaScript/TypeScript

**Documentation Format**:
```javascript
/**
 * Brief description of function purpose
 * @param {type} paramName - Description of parameter
 * @param {type} [optionalParam=default] - Optional parameter description
 * @returns {type} Description of return value
 * @throws {ErrorType} When this error occurs
 * @async
 */
```

**Key Features**:
- Support TypeScript type annotations
- Handle arrow functions and regular functions
- Mark async functions with `@async` tag
- Support generic types with `@template`
- Handle destructured parameters appropriately

#### 2.4 JavaDocumentationWriter (writers/java_writer.py)
**Purpose**: Generate Javadoc comments

**Documentation Format**:
```java
/**
 * Brief description of method purpose.
 * <p>
 * Detailed description if needed.
 *
 * @param paramName Description of parameter
 * @return Description of return value
 * @throws ExceptionClass When this exception occurs
 * @since 1.0
 */
```

**Key Features**:
- Extract parameter types from method signature
- Handle generic types (e.g., `List<String>`)
- Support constructor documentation
- Include `@since` tag for new methods

#### 2.5 CppDocumentationWriter (writers/cpp_writer.py)
**Purpose**: Generate Doxygen comments for C/C++

**Documentation Format**:
```cpp
/**
 * @brief Brief description of function purpose
 * 
 * Detailed description if needed.
 * 
 * @param paramName Description of parameter
 * @return Description of return value
 * @throw ExceptionClass When this exception occurs
 */
```

**Key Features**:
- Support both `/**` and `///` comment styles
- Handle pointer and reference parameters
- Document const methods appropriately
- Support template functions

#### 2.6 DocumentationInserter (writers/doc_inserter.py)
**Purpose**: Safely insert documentation into source files while preserving formatting

**Key Methods**:
- `insert_documentation(file_path: Path, items: List[DocItem]) -> bool`: Insert docs into file
- `create_backup(file_path: Path) -> Path`: Create backup before modification
- `validate_syntax(file_path: Path, language: str) -> bool`: Verify file still parses after changes
- `restore_backup(backup_path: Path, original_path: Path) -> None`: Restore on error

**Safety Features**:
- Create `.bak` backup before any modification
- Validate syntax after insertion (compile check for Python, parse check for others)
- Atomic file operations (write to temp, then rename)
- Preserve original file permissions and timestamps
- Maintain exact indentation of surrounding code
- Handle edge cases (file encoding, line endings, BOM)

**Insertion Algorithm**:
1. Read entire file into memory
2. Split into lines preserving line endings
3. For each undocumented item (sorted by line number, descending):
   - Generate appropriate documentation
   - Determine correct indentation from function/class definition
   - Insert documentation at correct line with proper indentation
4. Write modified content to temporary file
5. Validate syntax of temporary file
6. If valid, atomically replace original file
7. If invalid, restore from backup and report error

#### 2.7 DocumentationGenerator (core/doc_generator.py)
**Purpose**: Orchestrate the documentation generation process

**Key Methods**:
- `generate_documentation(scan_results: Dict, config: Dict) -> GenerationReport`: Main entry point
- `process_file(file_data: Dict) -> FileReport`: Process a single file
- `get_writer_for_language(language: str) -> BaseDocumentationWriter`: Factory method
- `calculate_coverage_improvement(before: float, after: float) -> Dict`: Calculate metrics

**Workflow**:
1. Load scan results (JSON output from scanner)
2. Filter for undocumented items
3. Group items by file and language
4. For each file:
   - Get appropriate writer for language
   - Generate documentation for all undocumented items
   - Use DocumentationInserter to modify file
   - Re-scan file to verify coverage improvement
5. Generate before/after coverage report
6. Return detailed generation report

### 3. CLI Integration (scanner.py modifications)

**New Arguments**:
```python
parser.add_argument(
    '--write-docs',
    action='store_true',
    help='Automatically generate and insert documentation for undocumented items'
)

parser.add_argument(
    '--dry-run',
    action='store_true',
    help='Show what would be documented without modifying files'
)

parser.add_argument(
    '--backup',
    action='store_true',
    default=True,
    help='Create backup files before modification (default: True)'
)

parser.add_argument(
    '--min-coverage',
    type=float,
    default=80.0,
    help='Target minimum documentation coverage percentage (default: 80.0)'
)
```

**Modified Workflow**:
```python
def main():
    # ... existing argument parsing ...
    
    # Run initial scan
    scan_results = scan_codebase(config, output_format=args.format)
    
    # If --write-docs flag is set
    if args.write_docs:
        logger.info("Starting documentation generation...")
        
        # Load scan results
        output_path = Path(config.get('output_file', 'output/documentation.json'))
        with open(output_path, 'r') as f:
            scan_data = json.load(f)
        
        # Generate documentation
        generator = DocumentationGenerator(
            logger=logger,
            dry_run=args.dry_run,
            create_backup=args.backup,
            min_coverage=args.min_coverage
        )
        
        report = generator.generate_documentation(scan_data, config)
        
        # Re-scan to verify improvements
        logger.info("Re-scanning to verify coverage improvements...")
        updated_results = scan_codebase(config, output_format=args.format)
        
        # Display before/after comparison
        display_coverage_comparison(report)
```

### 4. Coverage Comparison Report

**Report Format** (Markdown):
```markdown
# Documentation Generation Report

## Summary
- **Files Modified**: 12
- **Items Documented**: 156
- **Coverage Before**: 45.2%
- **Coverage After**: 87.8%
- **Improvement**: +42.6%

## By Language
| Language   | Before | After | Improvement | Items Added |
|------------|--------|-------|-------------|-------------|
| Python     | 52.1%  | 91.3% | +39.2%      | 89          |
| JavaScript | 38.7%  | 83.2% | +44.5%      | 45          |
| TypeScript | 41.2%  | 89.1% | +47.9%      | 22          |

## Modified Files
### src/utils/parser.py
- **Coverage**: 45% → 95% (+50%)
- **Items documented**: 15 functions
- **Status**: ✓ Success

### src/api/handlers.js
- **Coverage**: 30% → 85% (+55%)
- **Items documented**: 8 functions
- **Status**: ✓ Success

## Errors
- `src/legacy/old_code.py`: Syntax error after insertion (restored from backup)

## Remaining Gaps
- `tests/` directory: 23 test functions still undocumented
- `scripts/` directory: 5 utility scripts need documentation
```

### 5. Error Handling Strategy

**Error Categories**:
1. **File Access Errors**: Permission denied, file locked
   - Action: Skip file, log error, continue with others
   
2. **Syntax Errors After Insertion**: Generated doc breaks parsing
   - Action: Restore from backup, log detailed error, continue
   
3. **Encoding Errors**: Non-UTF-8 files
   - Action: Try alternative encodings (latin-1, cp1252), fallback to skip
   
4. **Parser Errors**: Cannot extract function signature
   - Action: Generate minimal documentation, log warning

**Backup Strategy**:
- Create `.bak` file before any modification
- Keep backups until successful re-scan
- Option to auto-delete backups on success
- Restore mechanism for failed operations

### 6. Testing Strategy

**Unit Tests** (writers/tests/):
- `test_python_writer.py`: Test Google-style docstring generation
- `test_javascript_writer.py`: Test JSDoc generation
- `test_java_writer.py`: Test Javadoc generation
- `test_cpp_writer.py`: Test Doxygen generation
- `test_doc_inserter.py`: Test safe file modification

**Integration Tests**:
- Test complete workflow with sample projects
- Test error recovery (syntax errors, permission errors)
- Test backup/restore mechanism
- Test coverage calculation accuracy

**Test Fixtures**:
- Sample undocumented files for each language
- Expected documentation output
- Edge cases (nested functions, decorators, generics)

### 7. Implementation Order

1. **Phase 1: Foundation** (Days 1-2)
   - Create `writers/` directory structure
   - Implement `BaseDocumentationWriter` abstract class
   - Implement `DocumentationInserter` with backup/restore

2. **Phase 2: Python Support** (Days 3-4)
   - Implement `PythonDocumentationWriter`
   - Add parameter inference logic
   - Create unit tests
   - Test with real Python files

3. **Phase 3: Multi-Language Support** (Days 5-7)
   - Implement `JavaScriptDocumentationWriter`
   - Implement `JavaDocumentationWriter`
   - Implement `CppDocumentationWriter`
   - Create language-specific tests

4. **Phase 4: Integration** (Days 8-9)
   - Implement `DocumentationGenerator` orchestrator
   - Integrate with `scanner.py` CLI
   - Add before/after coverage comparison
   - Create integration tests

5. **Phase 5: Polish & Documentation** (Day 10)
   - Add comprehensive error handling
   - Create user documentation
   - Add usage examples to README
   - Final testing and bug fixes

### 8. Success Criteria

**Functional Requirements**:
- ✓ Generate documentation for Python, JavaScript, Java, C++ files
- ✓ Insert documentation without breaking code syntax
- ✓ Preserve original code formatting and indentation
- ✓ Create backups before modification
- ✓ Calculate and report coverage improvements
- ✓ Handle errors gracefully with rollback capability

**Quality Requirements**:
- ✓ No placeholder text in generated documentation
- ✓ Parameter descriptions inferred from names/types
- ✓ All generated docs follow language-specific standards
- ✓ 100% of modified files remain syntactically valid
- ✓ Coverage improvement of at least 30% on typical codebases

**Performance Requirements**:
- Process 100 files in under 30 seconds
- Memory usage under 500MB for large codebases
- Atomic file operations to prevent corruption

### 9. Example Usage

```bash
# Scan and generate documentation for all undocumented items
python scanner.py --write-docs

# Dry run to see what would be documented
python scanner.py --write-docs --dry-run

# Target specific coverage threshold
python scanner.py --write-docs --min-coverage 90

# Scan specific directory and write docs
python scanner.py --root ./src --write-docs

# Generate docs for specific languages only
python scanner.py --languages python,javascript --write-docs

# Write docs and generate both JSON and Markdown reports
python scanner.py --write-docs --format both
```

### 10. Risk Mitigation

**Risk**: Generated documentation breaks code syntax
- **Mitigation**: Syntax validation after insertion, automatic rollback from backup

**Risk**: Loss of original code due to bugs
- **Mitigation**: Mandatory backup creation, atomic file operations, extensive testing

**Risk**: Poor quality generated documentation
- **Mitigation**: Parameter inference rules, validation against placeholders, manual review option

**Risk**: Performance issues with large codebases
- **Mitigation**: Process files in batches, optimize file I/O, parallel processing option

**Risk**: Encoding issues with non-UTF-8 files
- **Mitigation**: Multi-encoding support, graceful fallback, clear error messages

## Conclusion

This implementation plan provides a comprehensive roadmap for adding automatic documentation generation to the codebase scanner. The modular architecture allows for easy extension to additional languages, while the safety mechanisms ensure code integrity throughout the process.