# Tests Directory

This directory contains unit tests for the codebase scanner.

## Test Files

- `test_python_parser.py` - Tests for Python parser
- `test_detector.py` - Tests for language detector
- `test_filters.py` - Tests for file filtering utilities

## Running Tests

### Run All Tests

```bash
# From the codebase-scanner directory
python -m pytest tests/

# Or using unittest
python -m unittest discover tests/
```

### Run Specific Test File

```bash
# Using pytest
python -m pytest tests/test_python_parser.py

# Using unittest
python -m unittest tests.test_python_parser
```

### Run Specific Test Case

```bash
# Using pytest
python -m pytest tests/test_python_parser.py::TestPythonParser::test_simple_function

# Using unittest
python -m unittest tests.test_python_parser.TestPythonParser.test_simple_function
```

### Run with Verbose Output

```bash
python -m pytest tests/ -v

# Or with unittest
python -m unittest discover tests/ -v
```

## Test Coverage

To check test coverage (requires `coverage` package):

```bash
# Install coverage
pip install coverage

# Run tests with coverage
coverage run -m pytest tests/
coverage report
coverage html  # Generate HTML report
```

## Writing New Tests

### Test Structure

```python
import unittest
from pathlib import Path
import tempfile
from module_to_test import ClassToTest


class TestClassName(unittest.TestCase):
    """Test cases for ClassName."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Initialize test data
        pass
    
    def tearDown(self):
        """Clean up after tests."""
        # Clean up resources
        pass
    
    def test_feature_name(self):
        """Test specific feature."""
        # Arrange
        # Act
        # Assert
        pass


if __name__ == '__main__':
    unittest.main()
```

### Best Practices

1. **One test per feature**: Each test should verify one specific behavior
2. **Descriptive names**: Use clear, descriptive test method names
3. **Arrange-Act-Assert**: Structure tests with setup, execution, and verification
4. **Clean up**: Always clean up temporary files and resources
5. **Independent tests**: Tests should not depend on each other
6. **Edge cases**: Test boundary conditions and error cases

## Test Categories

### Unit Tests (Current)
- Test individual components in isolation
- Fast execution
- No external dependencies

### Integration Tests (Future)
- Test component interactions
- Test with real file systems
- Test end-to-end workflows

### Performance Tests (Future)
- Test with large codebases
- Measure execution time
- Memory usage profiling

## Adding Tests for New Parsers

When adding a new language parser, create a corresponding test file:

```python
# tests/test_mylang_parser.py
import unittest
from parsers.mylang_parser import MyLangParser

class TestMyLangParser(unittest.TestCase):
    def test_function_parsing(self):
        # Test function extraction
        pass
    
    def test_class_parsing(self):
        # Test class extraction
        pass
    
    def test_documentation_extraction(self):
        # Test docstring/comment extraction
        pass
```

## Continuous Integration

These tests can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - run: python -m unittest discover tests/
```

## Current Test Coverage

| Module | Coverage | Tests |
|--------|----------|-------|
| Python Parser | ✅ Basic | 8 tests |
| Language Detector | ✅ Basic | 11 tests |
| File Filters | ✅ Basic | 9 tests |
| JavaScript Parser | ⏳ Pending | - |
| Java Parser | ⏳ Pending | - |
| C/C++ Parser | ⏳ Pending | - |
| Walker | ⏳ Pending | - |
| Extractor | ⏳ Pending | - |
| Formatter | ⏳ Pending | - |

## Known Issues

None currently. Report issues in the main project repository.

## Contributing

When contributing new features:
1. Write tests first (TDD approach)
2. Ensure all existing tests pass
3. Add tests for new functionality
4. Update this README if needed