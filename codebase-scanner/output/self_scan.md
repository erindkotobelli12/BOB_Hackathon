# 📚 Documentation Report: codebase-scanner

**Generated:** 2026-05-01 16:01:38 UTC
**Root Directory:** `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner`

## 📊 Coverage Summary

| Language | Files | Functions | Coverage % |
|----------|-------|-----------|------------|
| python | 24 | 129 | 100.0% |
| **Total** | **24** | **129** | **100.0%** |

## ✅ All Items Documented

Congratulations! All functions and methods have documentation.

## 📄 File Documentation

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\core\__init__.py`

**Language:** python

_No functions or classes found._

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\core\detector.py`

**Language:** python

#### Classes

##### Class: `LanguageDetector`

**Line:** 7

**Documentation:**

> Detects programming language from file extensions and content.

**Methods:**

- **`detect_language(cls, file_path)`** (Line 48)
  - Returns: `Optional[str]`
  - Detect the programming language of a file.

- **`_detect_from_shebang(cls, file_path)`** (Line 72)
  - Returns: `Optional[str]`
  - Detect language from shebang line.

- **`get_supported_languages(cls)`** (Line 99)
  - Returns: `list[str]`
  - Get list of supported languages.

- **`get_extensions_for_language(cls, language)`** (Line 109)
  - Returns: `list[str]`
  - Get file extensions for a specific language.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\core\extractor.py`

**Language:** python

#### Classes

##### Class: `MetadataExtractor`

**Line:** 16

**Documentation:**

> Extracts metadata from source files using appropriate parsers.

**Methods:**

- **`__init__(self, logger)`** (Line 29)
  - Returns: `None`
  - Initialize metadata extractor.

- **`extract(self, file_path)`** (Line 39)
  - Returns: `Dict[str, Any]`
  - Extract metadata from a file.

- **`_use_generic_parser(self, file_path)`** (Line 72)
  - Returns: `Dict[str, Any]`
  - Use generic parser as fallback.

- **`_error_result(self, file_path, error)`** (Line 78)
  - Returns: `Dict[str, Any]`
  - Return error result structure.

- **`get_supported_languages(self)`** (Line 92)
  - Returns: `list[str]`
  - Get list of languages with dedicated parsers.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\core\walker.py`

**Language:** python

#### Classes

##### Class: `DirectoryWalker`

**Line:** 9

**Documentation:**

> Walks through directory structure and yields files for scanning.

**Methods:**

- **`__init__(self, root_dir, exclude_patterns, include_extensions, max_file_size_mb, follow_symlinks, logger)`** (Line 12)
  - Returns: `None`
  - Initialize directory walker.

- **`walk(self)`** (Line 48)
  - Returns: `Iterator[Path]`
  - Walk through directory and yield files to scan.

- **`_walk_recursive(self, directory)`** (Line 73)
  - Returns: `Iterator[Path]`
  - Recursively walk through directory.

- **`_should_process_file(self, file_path)`** (Line 108)
  - Returns: `bool`
  - Check if a file should be processed.

- **`_log_stats(self)`** (Line 150)
  - Returns: `None`
  - Log statistics about the walk.

- **`get_stats(self)`** (Line 160)
  - Returns: `dict`
  - Get walk statistics.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\formatters\__init__.py`

**Language:** python

_No functions or classes found._

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\formatters\json_formatter.py`

**Language:** python

#### Classes

##### Class: `JSONFormatter`

**Line:** 9

**Documentation:**

> Formats scan results as JSON.

**Methods:**

- **`format(files_data, root_directory, coverage_report)`** (Line 13)
  - Returns: `Dict[str, Any]`
  - Format scan results as structured JSON.

- **`save(data, output_path)`** (Line 52)
  - Returns: `None`
  - Save formatted data to JSON file.

- **`calculate_coverage_report(files_data)`** (Line 68)
  - Returns: `Dict[str, Any]`
  - Calculate documentation coverage report.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\formatters\markdown_formatter.py`

**Language:** python

#### Classes

##### Class: `MarkdownFormatter`

**Line:** 8

**Documentation:**

> Formats scan results as human-readable Markdown documentation.

**Methods:**

- **`format(files_data, root_directory, coverage_report)`** (Line 12)
  - Returns: `str`
  - Format scan results as Markdown documentation.

- **`_calculate_language_stats(files_data)`** (Line 153)
  - Returns: `Dict[str, Dict[str, int]]`
  - Calculate statistics per language.

- **`_format_function(func)`** (Line 183)
  - Returns: `List[str]`
  - Format a function as markdown.

- **`_format_class(cls)`** (Line 239)
  - Returns: `List[str]`
  - Format a class as markdown.

- **`save(content, output_path)`** (Line 302)
  - Returns: `None`
  - Save formatted markdown content to file.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\parsers\__init__.py`

**Language:** python

_No functions or classes found._

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\parsers\base_parser.py`

**Language:** python

#### Classes

##### Class: `BaseParser`

**Line:** 8

**Documentation:**

> Abstract base class for language parsers.

**Methods:**

- **`__init__(self, file_path)`** (Line 11)
  - Returns: `None`
  - Initialize parser.

- **`load_file(self)`** (Line 23)
  - Returns: `bool`
  - Load file content.

- **`parse(self)`** (Line 41)
  - Returns: `Dict[str, Any]`
  - Parse the file and extract metadata.

- **`get_file_metadata(self)`** (Line 56)
  - Returns: `Dict[str, Any]`
  - Get basic file metadata.

- **`calculate_coverage(documented_items, total_items)`** (Line 70)
  - Returns: `float`
  - Calculate documentation coverage percentage.

- **`extract_docstring(lines, start_line)`** (Line 86)
  - Returns: `Optional[str]`
  - Extract docstring from lines starting at given position.

- **`clean_comment(comment)`** (Line 125)
  - Returns: `str`
  - Clean comment text by removing comment markers.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\parsers\cpp_parser.py`

**Language:** python

#### Classes

##### Class: `CppParser`

**Line:** 9

**Documentation:**

> Parser for C and C++ source files.

**Methods:**

- **`__init__(self, file_path)`** (Line 30)
  - Returns: `None`
  - Initialize C/C++ parser.

- **`parse(self)`** (Line 40)
  - Returns: `Dict[str, Any]`
  - Parse C/C++ file and extract metadata.

- **`_extract_classes(self)`** (Line 75)
  - Returns: `List[Dict[str, Any]]`
  - Extract class/struct definitions (C++ only).

- **`_extract_methods(self, class_body, class_line_start)`** (Line 128)
  - Returns: `List[Dict[str, Any]]`
  - Extract method definitions from class body.

- **`_extract_functions(self)`** (Line 168)
  - Returns: `List[Dict[str, Any]]`
  - Extract function definitions.

- **`_parse_parameters(self, params_str)`** (Line 215)
  - Returns: `List[Dict[str, Any]]`
  - Parse function parameters.

- **`_extract_includes(self)`** (Line 247)
  - Returns: `List[str]`
  - Extract include statements.

- **`_extract_doxygen_before(self, position)`** (Line 256)
  - Returns: `Optional[str]`
  - Extract Doxygen comment before a position.

- **`_extract_doxygen_before_in_text(self, text, position)`** (Line 283)
  - Returns: `Optional[str]`
  - Extract Doxygen comment before a position in given text.

- **`_clean_doxygen(self, doxygen)`** (Line 296)
  - Returns: `str`
  - Clean Doxygen comment text.

- **`_extract_visibility(self, text, position)`** (Line 310)
  - Returns: `str`
  - Extract visibility modifier from class body.

- **`_empty_result(self)`** (Line 329)
  - Returns: `Dict[str, Any]`
  - Return empty result structure.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\parsers\generic_parser.py`

**Language:** python

#### Classes

##### Class: `GenericParser`

**Line:** 8

**Documentation:**

> Fallback parser for languages without specific support.

**Methods:**

- **`__init__(self, file_path)`** (Line 11)
  - Returns: `None`
  - Initialize generic parser.

- **`parse(self)`** (Line 20)
  - Returns: `Dict[str, Any]`
  - Parse file with basic metadata only.

- **`_empty_result(self)`** (Line 42)
  - Returns: `Dict[str, Any]`
  - Return empty result structure.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\parsers\java_parser.py`

**Language:** python

#### Classes

##### Class: `JavaParser`

**Line:** 9

**Documentation:**

> Parser for Java source files.

**Methods:**

- **`__init__(self, file_path)`** (Line 30)
  - Returns: `None`
  - Initialize Java parser.

- **`parse(self)`** (Line 39)
  - Returns: `Dict[str, Any]`
  - Parse Java file and extract metadata.

- **`_extract_classes(self)`** (Line 71)
  - Returns: `List[Dict[str, Any]]`
  - Extract class definitions.

- **`_extract_methods(self, class_body, class_line_start)`** (Line 121)
  - Returns: `List[Dict[str, Any]]`
  - Extract method definitions from class body.

- **`_parse_parameters(self, params_str)`** (Line 157)
  - Returns: `List[Dict[str, Any]]`
  - Parse method parameters.

- **`_parse_single_parameter(self, param)`** (Line 183)
  - Returns: `Dict[str, Any]`
  - Parse a single parameter.

- **`_extract_imports(self)`** (Line 212)
  - Returns: `List[str]`
  - Extract import statements.

- **`_extract_javadoc_before(self, position)`** (Line 221)
  - Returns: `Optional[str]`
  - Extract Javadoc comment before a position.

- **`_extract_javadoc_before_in_text(self, text, position)`** (Line 234)
  - Returns: `Optional[str]`
  - Extract Javadoc comment before a position in given text.

- **`_clean_javadoc(self, javadoc)`** (Line 247)
  - Returns: `str`
  - Clean Javadoc comment text.

- **`_extract_visibility(self, text)`** (Line 261)
  - Returns: `str`
  - Extract visibility modifier.

- **`_extract_annotations(self, text, position)`** (Line 271)
  - Returns: `List[str]`
  - Extract annotations before a method.

- **`_empty_result(self)`** (Line 283)
  - Returns: `Dict[str, Any]`
  - Return empty result structure.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\parsers\javascript_parser.py`

**Language:** python

#### Classes

##### Class: `JavaScriptParser`

**Line:** 9

**Documentation:**

> Parser for JavaScript and TypeScript files.

**Methods:**

- **`__init__(self, file_path)`** (Line 38)
  - Returns: `None`
  - Initialize JavaScript/TypeScript parser.

- **`parse(self)`** (Line 48)
  - Returns: `Dict[str, Any]`
  - Parse JavaScript/TypeScript file and extract metadata.

- **`_extract_classes(self)`** (Line 83)
  - Returns: `List[Dict[str, Any]]`
  - Extract class definitions.

- **`_extract_methods(self, class_body, class_line_start)`** (Line 127)
  - Returns: `List[Dict[str, Any]]`
  - Extract method definitions from class body.

- **`_extract_functions(self)`** (Line 161)
  - Returns: `List[Dict[str, Any]]`
  - Extract top-level function definitions.

- **`_parse_parameters(self, params_str)`** (Line 207)
  - Returns: `List[Dict[str, Any]]`
  - Parse function parameters.

- **`_extract_imports(self)`** (Line 246)
  - Returns: `List[str]`
  - Extract import statements.

- **`_extract_jsdoc_before(self, position)`** (Line 255)
  - Returns: `Optional[str]`
  - Extract JSDoc comment before a position.

- **`_extract_jsdoc_before_in_text(self, text, position)`** (Line 270)
  - Returns: `Optional[str]`
  - Extract JSDoc comment before a position in given text.

- **`_clean_jsdoc(self, jsdoc)`** (Line 283)
  - Returns: `str`
  - Clean JSDoc comment text.

- **`_get_visibility(self, name)`** (Line 297)
  - Returns: `str`
  - Determine visibility from name.

- **`_empty_result(self)`** (Line 303)
  - Returns: `Dict[str, Any]`
  - Return empty result structure.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\parsers\python_parser.py`

**Language:** python

#### Classes

##### Class: `PythonParser`

**Line:** 9

**Documentation:**

> Parser for Python source files using AST.

**Methods:**

- **`__init__(self, file_path)`** (Line 12)
  - Returns: `None`
  - Initialize Python parser.

- **`parse(self)`** (Line 22)
  - Returns: `Dict[str, Any]`
  - Parse Python file and extract metadata.

- **`_extract_classes(self)`** (Line 63)
  - Returns: `List[Dict[str, Any]]`
  - Extract class definitions from AST.

- **`_extract_methods(self, class_node)`** (Line 85)
  - Returns: `List[Dict[str, Any]]`
  - Extract method definitions from a class.

- **`_extract_functions(self)`** (Line 97)
  - Returns: `List[Dict[str, Any]]`
  - Extract top-level function definitions.

- **`_extract_function_info(self, node)`** (Line 110)
  - Returns: `Dict[str, Any]`
  - Extract information from a function node.

- **`_extract_parameters(self, node)`** (Line 123)
  - Returns: `List[Dict[str, Any]]`
  - Extract function parameters with type hints and defaults.

- **`_extract_imports(self)`** (Line 160)
  - Returns: `List[str]`
  - Extract import statements.

- **`_get_annotation(self, annotation)`** (Line 178)
  - Returns: `Optional[str]`
  - Get string representation of type annotation.

- **`_get_return_annotation(self, node)`** (Line 184)
  - Returns: `Optional[str]`
  - Get return type annotation.

- **`_get_default_value(self, node)`** (Line 190)
  - Returns: `Optional[str]`
  - Get string representation of default value.

- **`_get_decorator_name(self, decorator)`** (Line 197)
  - Returns: `str`
  - Get decorator name.

- **`_get_name(self, node)`** (Line 205)
  - Returns: `str`
  - Get name from AST node.

- **`_get_visibility(self, name)`** (Line 211)
  - Returns: `str`
  - Determine visibility from name.

- **`_empty_result(self)`** (Line 219)
  - Returns: `Dict[str, Any]`
  - Return empty result structure.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\run_tests.py`

**Language:** python

_No functions or classes found._

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\scanner.py`

**Language:** python

#### Functions

##### `load_config(config_path)`

**Line:** 16 | **Returns:** `Dict[str, Any]`

**Parameters:**
- `config_path` (Path)

**Documentation:**

> Load configuration from JSON file.
> 
> Args:
>     config_path: Path to config file
>     
> Returns:
>     Configuration dictionary

##### `scan_codebase(config, output_format)`

**Line:** 34 | **Returns:** `None`

**Parameters:**
- `config` (Dict[str, Any])
- `output_format` (str)

**Documentation:**

> Scan codebase and generate documentation metadata.
> 
> Args:
>     config: Configuration dictionary
>     output_format: Output format ('json', 'markdown', or 'both')

##### `main()`

**Line:** 123 | **Returns:** `None`

**Documentation:**

> Main entry point.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\tests\__init__.py`

**Language:** python

_No functions or classes found._

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\tests\conftest.py`

**Language:** python

_No functions or classes found._

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\tests\test_detector.py`

**Language:** python

#### Classes

##### Class: `TestLanguageDetector`

**Line:** 10

**Documentation:**

> Test cases for LanguageDetector.

**Methods:**

- **`setUp(self)`** (Line 13)
  - Returns: `None`
  - Set up test fixtures.

- **`tearDown(self)`** (Line 18)
  - Returns: `None`
  - Clean up test fixtures.

- **`create_temp_file(self, filename, content)`** (Line 24)
  - Returns: `Path`
  - Create a temporary file for testing.

- **`test_python_detection(self)`** (Line 31)
  - Returns: `None`
  - Test Python file detection.

- **`test_javascript_detection(self)`** (Line 37)
  - Returns: `None`
  - Test JavaScript file detection.

- **`test_typescript_detection(self)`** (Line 43)
  - Returns: `None`
  - Test TypeScript file detection.

- **`test_java_detection(self)`** (Line 49)
  - Returns: `None`
  - Test Java file detection.

- **`test_c_detection(self)`** (Line 55)
  - Returns: `None`
  - Test C file detection.

- **`test_cpp_detection(self)`** (Line 61)
  - Returns: `None`
  - Test C++ file detection.

- **`test_shebang_python(self)`** (Line 67)
  - Returns: `None`
  - Test Python detection via shebang.

- **`test_unknown_extension(self)`** (Line 74)
  - Returns: `None`
  - Test unknown file extension.

- **`test_get_supported_languages(self)`** (Line 80)
  - Returns: `None`
  - Test getting list of supported languages.

- **`test_get_extensions_for_language(self)`** (Line 87)
  - Returns: `None`
  - Test getting extensions for a language.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\tests\test_filters.py`

**Language:** python

#### Classes

##### Class: `TestFilters`

**Line:** 10

**Documentation:**

> Test cases for file filtering utilities.

**Methods:**

- **`setUp(self)`** (Line 13)
  - Returns: `None`
  - Set up test fixtures.

- **`tearDown(self)`** (Line 17)
  - Returns: `None`
  - Clean up test fixtures.

- **`test_should_exclude_path_simple(self)`** (Line 23)
  - Returns: `None`
  - Test simple exclusion pattern.

- **`test_should_exclude_path_no_match(self)`** (Line 29)
  - Returns: `None`
  - Test path that should not be excluded.

- **`test_should_exclude_path_wildcard(self)`** (Line 35)
  - Returns: `None`
  - Test wildcard exclusion pattern.

- **`test_matches_extension_positive(self)`** (Line 41)
  - Returns: `None`
  - Test matching file extension.

- **`test_matches_extension_negative(self)`** (Line 47)
  - Returns: `None`
  - Test non-matching file extension.

- **`test_matches_extension_case_insensitive(self)`** (Line 53)
  - Returns: `None`
  - Test case-insensitive extension matching.

- **`test_get_file_size_mb(self)`** (Line 59)
  - Returns: `None`
  - Test file size calculation.

- **`test_is_binary_file_text(self)`** (Line 69)
  - Returns: `None`
  - Test text file detection.

- **`test_is_binary_file_binary(self)`** (Line 77)
  - Returns: `None`
  - Test binary file detection.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\tests\test_python_parser.py`

**Language:** python

#### Classes

##### Class: `TestPythonParser`

**Line:** 10

**Documentation:**

> Test cases for PythonParser.

**Methods:**

- **`setUp(self)`** (Line 13)
  - Returns: `None`
  - Set up test fixtures.

- **`tearDown(self)`** (Line 17)
  - Returns: `None`
  - Clean up test fixtures.

- **`create_temp_file(self, filename, content)`** (Line 24)
  - Returns: `Path`
  - Create a temporary Python file for testing.

- **`test_simple_function(self)`** (Line 31)
  - Returns: `None`
  - Test parsing a simple function.

- **`test_class_with_methods(self)`** (Line 51)
  - Returns: `None`
  - Test parsing a class with methods.

- **`test_async_function(self)`** (Line 76)
  - Returns: `None`
  - Test parsing async function.

- **`test_decorated_function(self)`** (Line 90)
  - Returns: `None`
  - Test parsing decorated function.

- **`test_imports(self)`** (Line 105)
  - Returns: `None`
  - Test parsing import statements.

- **`test_documentation_coverage(self)`** (Line 122)
  - Returns: `None`
  - Test documentation coverage calculation.

- **`test_no_docstring_function(self)`** (Line 139)
  - Returns: `None`
  - Test documentation coverage with no docstring.

- **`test_syntax_error(self)`** (Line 154)
  - Returns: `None`
  - Test handling of syntax errors.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\utils\__init__.py`

**Language:** python

_No functions or classes found._

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\utils\filters.py`

**Language:** python

#### Functions

##### `should_exclude_path(path, exclude_patterns)`

**Line:** 8 | **Returns:** `bool`

**Parameters:**
- `path` (Path)
- `exclude_patterns` (List[str])

**Documentation:**

> Check if a path should be excluded based on patterns.
> 
> Args:
>     path: Path to check
>     exclude_patterns: List of glob patterns to exclude
>     
> Returns:
>     True if path should be excluded, False otherwise

##### `matches_extension(path, extensions)`

**Line:** 36 | **Returns:** `bool`

**Parameters:**
- `path` (Path)
- `extensions` (List[str])

**Documentation:**

> Check if a file has one of the specified extensions.
> 
> Args:
>     path: Path to check
>     extensions: List of file extensions (e.g., ['.py', '.js'])
>     
> Returns:
>     True if file extension matches, False otherwise

##### `get_file_size_mb(path)`

**Line:** 50 | **Returns:** `float`

**Parameters:**
- `path` (Path)

**Documentation:**

> Get file size in megabytes.
> 
> Args:
>     path: Path to file
>     
> Returns:
>     File size in MB

##### `is_binary_file(path, sample_size)`

**Line:** 66 | **Returns:** `bool`

**Parameters:**
- `path` (Path)
- `sample_size` (int)

**Documentation:**

> Check if a file is binary by reading a sample.
> 
> Args:
>     path: Path to file
>     sample_size: Number of bytes to sample
>     
> Returns:
>     True if file appears to be binary, False otherwise

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\codebase-scanner\utils\logger.py`

**Language:** python

#### Functions

##### `setup_logger(name, verbose, log_file)`

**Line:** 9 | **Returns:** `logging.Logger`

**Parameters:**
- `name` (str)
- `verbose` (bool)
- `log_file` (str | None)

**Documentation:**

> Set up and configure a logger for the application.
> 
> Args:
>     name: Logger name
>     verbose: If True, set level to DEBUG, otherwise INFO
>     log_file: Optional path to log file
>     
> Returns:
>     Configured logger instance

##### `log_scan_summary(logger, stats)`

**Line:** 52 | **Returns:** `None`

**Parameters:**
- `logger` (logging.Logger)
- `stats` (dict)

**Documentation:**

> Log a summary of the scan results.
> 
> Args:
>     logger: Logger instance
>     stats: Dictionary containing scan statistics

---

## 📈 Summary Statistics

- **Total Files Scanned:** 24
- **Total Functions/Methods:** 129
- **Total Classes:** 14
- **Documentation Coverage:** 100.0%
- **Documented Items:** 129
- **Undocumented Items:** 0

---

_Generated by Codebase Scanner_