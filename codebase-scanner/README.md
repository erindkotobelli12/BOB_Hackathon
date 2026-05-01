# Codebase Scanner

A powerful, extensible file scanner that walks through codebases, extracts functions and classes, and generates structured documentation metadata in JSON format.

## Features

- 🔍 **Multi-Language Support**: Python, JavaScript, TypeScript, Java, C, C++
- 📊 **Documentation Coverage Analysis**: Calculate and report documentation coverage
- 🎯 **Smart Filtering**: Exclude patterns, file size limits, binary file detection
- 🔧 **Extensible Architecture**: Easy to add support for new languages
- 📝 **Rich Metadata Extraction**: Functions, classes, parameters, return types, docstrings
- ⚙️ **Configurable**: JSON-based configuration with CLI overrides
- 📈 **Detailed Reporting**: JSON output with comprehensive scan statistics

## Installation

### Prerequisites

- Python 3.8 or higher

### Setup

1. Clone or download the codebase-scanner directory
2. Navigate to the directory:
   ```bash
   cd codebase-scanner
   ```

3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

No external dependencies required! The scanner uses only Python standard library.

## Quick Start

### Basic Usage

```bash
# Scan current directory with default config
python scanner.py

# Scan specific directory
python scanner.py --root /path/to/project

# Use custom config file
python scanner.py --config my-config.json

# Specify output file
python scanner.py --output results.json
```

### First Run

On first run, if no config file exists, the scanner will create a default `config.json`:

```bash
python scanner.py
```

This creates a config file with sensible defaults that you can customize.

## Configuration

### Config File (config.json)

```json
{
  "root_directory": ".",
  "output_file": "output/documentation.json",
  "exclude_patterns": [
    "node_modules/**",
    "venv/**",
    "env/**",
    "__pycache__/**",
    "*.min.js",
    "dist/**",
    "build/**",
    ".git/**"
  ],
  "include_extensions": [
    ".py", ".js", ".ts", ".jsx", ".tsx",
    ".java", ".c", ".cpp", ".h", ".hpp"
  ],
  "max_file_size_mb": 10,
  "follow_symlinks": false,
  "extract_imports": true,
  "calculate_coverage": true,
  "verbose_logging": true
}
```

### Configuration Options

| Option | Type | Description |
|--------|------|-------------|
| `root_directory` | string | Root directory to scan |
| `output_file` | string | Path to output JSON file |
| `exclude_patterns` | array | Glob patterns to exclude |
| `include_extensions` | array | File extensions to include |
| `max_file_size_mb` | number | Maximum file size in MB |
| `follow_symlinks` | boolean | Whether to follow symbolic links |
| `extract_imports` | boolean | Extract import statements |
| `calculate_coverage` | boolean | Calculate documentation coverage |
| `verbose_logging` | boolean | Enable verbose logging |

## Command Line Options

```bash
python scanner.py [OPTIONS]

Options:
  --config PATH       Path to configuration file (default: config.json)
  --root PATH         Root directory to scan (overrides config)
  --output PATH       Output file path (overrides config)
  --languages LANGS   Comma-separated list of languages (e.g., python,javascript)
  --verbose           Enable verbose logging
  -h, --help          Show help message
```

## Usage Examples

### Scan Python Project

```bash
python scanner.py --root /path/to/python-project --languages python
```

### Scan JavaScript/TypeScript Project

```bash
python scanner.py --root /path/to/js-project --languages javascript,typescript
```

### Scan with Custom Exclusions

Create a custom config file:

```json
{
  "root_directory": "./src",
  "exclude_patterns": [
    "tests/**",
    "*.test.js",
    "node_modules/**"
  ],
  "include_extensions": [".js", ".jsx"]
}
```

Run with custom config:

```bash
python scanner.py --config custom-config.json
```

### Scan Multiple Languages

```bash
python scanner.py --root /path/to/project --languages python,java,cpp
```

## Output Format

The scanner generates a JSON file with the following structure:

```json
{
  "scan_metadata": {
    "timestamp": "2026-05-01T14:00:00Z",
    "root_directory": "/path/to/project",
    "total_files": 150,
    "total_functions": 450,
    "total_classes": 120,
    "languages_detected": ["python", "javascript"]
  },
  "files": [
    {
      "path": "src/utils.py",
      "language": "python",
      "size_bytes": 2048,
      "line_count": 85,
      "classes": [
        {
          "name": "DataProcessor",
          "line_start": 10,
          "line_end": 45,
          "docstring": "Processes data from various sources",
          "methods": [
            {
              "name": "process",
              "line_start": 15,
              "line_end": 30,
              "parameters": [
                {
                  "name": "data",
                  "type": "dict",
                  "default": null
                }
              ],
              "return_type": "ProcessedData",
              "docstring": "Process input data",
              "decorators": ["@staticmethod"],
              "is_async": false,
              "visibility": "public"
            }
          ],
          "base_classes": ["BaseProcessor"],
          "decorators": []
        }
      ],
      "functions": [
        {
          "name": "calculate_sum",
          "line_start": 50,
          "line_end": 55,
          "parameters": [
            {
              "name": "numbers",
              "type": "List[int]",
              "default": null
            }
          ],
          "return_type": "int",
          "docstring": "Calculate sum of numbers",
          "decorators": [],
          "is_async": false
        }
      ],
      "imports": [
        "from typing import List",
        "import json"
      ],
      "documentation_coverage": 85.5
    }
  ],
  "coverage_report": {
    "overall_coverage": 72.3,
    "total_items": 570,
    "documented_items": 412,
    "undocumented_items_count": 158,
    "by_language": {
      "python": 85.0,
      "javascript": 65.5
    },
    "undocumented_items": [
      {
        "file": "src/api.js",
        "type": "function",
        "name": "handleRequest",
        "line": 45
      }
    ]
  }
}
```

## Supported Languages

### Python (.py)
- ✅ Functions and methods
- ✅ Classes with inheritance
- ✅ Docstrings (Google, NumPy formats)
- ✅ Type hints
- ✅ Decorators
- ✅ Async functions
- ✅ Import statements

### JavaScript/TypeScript (.js, .jsx, .ts, .tsx)
- ✅ Functions and arrow functions
- ✅ Classes and methods
- ✅ JSDoc comments
- ✅ Type annotations (TypeScript)
- ✅ Async functions
- ✅ Import statements

### Java (.java)
- ✅ Classes and methods
- ✅ Javadoc comments
- ✅ Interfaces and inheritance
- ✅ Annotations
- ✅ Access modifiers
- ✅ Import statements

### C/C++ (.c, .cpp, .h, .hpp)
- ✅ Functions
- ✅ Classes and methods (C++)
- ✅ Doxygen comments
- ✅ Structs
- ✅ Include statements

## Extending the Scanner

### Adding a New Language

1. Create a new parser in `parsers/`:

```python
# parsers/my_language_parser.py
from .base_parser import BaseParser

class MyLanguageParser(BaseParser):
    def parse(self):
        # Implement parsing logic
        pass
```

2. Register the parser in `core/extractor.py`:

```python
PARSER_MAP = {
    'python': PythonParser,
    'mylang': MyLanguageParser,  # Add your parser
    # ...
}
```

3. Add language detection in `core/detector.py`:

```python
EXTENSION_MAP = {
    '.py': 'python',
    '.ml': 'mylang',  # Add your extension
    # ...
}
```

## Project Structure

```
codebase-scanner/
├── scanner.py              # Main entry point
├── config.json            # Configuration file
├── core/
│   ├── walker.py         # Directory traversal
│   ├── detector.py       # Language detection
│   └── extractor.py      # Metadata extraction
├── parsers/
│   ├── base_parser.py    # Abstract base class
│   ├── python_parser.py  # Python parser
│   ├── javascript_parser.py  # JS/TS parser
│   ├── java_parser.py    # Java parser
│   ├── cpp_parser.py     # C/C++ parser
│   └── generic_parser.py # Fallback parser
├── formatters/
│   └── json_formatter.py # JSON output
├── utils/
│   ├── logger.py         # Logging
│   └── filters.py        # File filtering
├── output/               # Generated output
└── README.md            # This file
```

## Troubleshooting

### Common Issues

**Issue**: "Config file not found"
- **Solution**: Run `python scanner.py` to create a default config file

**Issue**: "Root directory does not exist"
- **Solution**: Check the `root_directory` path in config.json or use `--root` flag

**Issue**: "No files found"
- **Solution**: Check `include_extensions` and `exclude_patterns` in config

**Issue**: Parsing errors for specific files
- **Solution**: Check logs for details. The scanner continues on errors.

### Debug Mode

Enable verbose logging for detailed information:

```bash
python scanner.py --verbose
```

Or in config.json:
```json
{
  "verbose_logging": true
}
```

## Performance Tips

1. **Exclude unnecessary directories**: Add patterns like `node_modules/**`, `venv/**` to `exclude_patterns`
2. **Limit file size**: Set appropriate `max_file_size_mb` to skip large files
3. **Filter by language**: Use `--languages` flag to scan only specific languages
4. **Disable symlinks**: Set `follow_symlinks: false` to avoid circular references

## Use Cases

### Documentation Generation
Extract metadata to generate API documentation automatically

### Code Analysis
Analyze codebase structure and documentation coverage

### Migration Planning
Understand codebase before refactoring or migration

### Quality Metrics
Track documentation coverage over time

### IDE Integration
Use output for code intelligence features

## Contributing

To contribute a new language parser:

1. Extend `BaseParser` class
2. Implement the `parse()` method
3. Add language detection rules
4. Register in `PARSER_MAP`
5. Add tests

## License

This project is provided as-is for educational and commercial use.

## Support

For issues or questions:
- Check the troubleshooting section
- Review the configuration options
- Enable verbose logging for details

## Changelog

### Version 1.0.0
- Initial release
- Support for Python, JavaScript, TypeScript, Java, C, C++
- Documentation coverage analysis
- JSON output format
- Configurable scanning options