# Using the --write-docs Feature

## Overview

The `--write-docs` flag enables automatic generation of Google-style docstrings for undocumented Python functions, methods, and classes using IBM watsonx.ai's granite-3-8b-instruct model.

## Setup

### 1. Configure Environment Variables

Copy the example environment file and add your credentials:

```bash
cp .env.example .env
```

Edit `.env` and add your watsonx.ai credentials:

```bash
WATSONX_API_KEY=your_actual_api_key_here
WATSONX_PROJECT_ID=your_actual_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
```

### 2. Verify Installation

Ensure all dependencies are available (no external packages required - uses only Python stdlib):

```bash
cd codebase-scanner
python scanner.py --help
```

You should see the `--write-docs` option in the help output.

## Usage

### Basic Usage

Scan a directory and generate missing docstrings:

```bash
python scanner.py --write-docs
```

This will:
1. Scan all Python files in the current directory
2. Identify functions, methods, and classes without docstrings
3. Generate Google-style docstrings using watsonx.ai
4. Insert the docstrings directly into the source files
5. Print a progress report

### Scan Specific Directory

```bash
python scanner.py --root /path/to/project --write-docs
```

### Scan Only Python Files

```bash
python scanner.py --languages python --write-docs
```

### Generate Documentation and Save Report

```bash
python scanner.py --write-docs --format both --output results.json
```

This generates:
- `results.json` - Scan metadata with coverage statistics
- `results.md` - Markdown documentation report
- Modified source files with new docstrings

## Example

### Before

```python
def calculate_sum(a, b):
    return a + b
```

### After Running --write-docs

```python
def calculate_sum(a, b):
    """
    Calculate the sum of two numbers.
    
    Args:
        a: First number to add
        b: Second number to add
    
    Returns:
        The sum of a and b
    """
    return a + b
```

## Output Report

The tool prints a detailed report:

```
============================================================
Documentation Generation Report
============================================================
Files processed:       15
Files modified:        8
Functions documented:  23
Classes documented:    5
Methods documented:    12
Total items documented: 40
============================================================
```

## Features

- **Google-style docstrings**: Generates properly formatted docstrings with Args, Returns, and Raises sections
- **AST-based insertion**: Uses Python's AST module for accurate code modification
- **No placeholders**: Validates that generated docstrings don't contain TODO or placeholder text
- **Preserves formatting**: Maintains original code indentation and structure
- **Progress tracking**: Shows detailed statistics about documentation generation

## Limitations

- Only supports Python files (`.py` extension)
- Requires valid watsonx.ai credentials
- Modifies source files in-place (make backups first!)
- Skips files with syntax errors
- Only documents items that don't already have docstrings

## Troubleshooting

### "WATSONX_API_KEY environment variable not set"

Make sure you've created a `.env` file with your credentials in the `codebase-scanner` directory.

### "Error generating docstring: HTTP 401"

Your API key may be invalid or expired. Check your watsonx.ai credentials.

### "Error generating docstring: HTTP 429"

You've hit the API rate limit. Wait a moment and try again.

### Files not being modified

- Check that functions/classes don't already have docstrings
- Verify the file has valid Python syntax
- Check the log output for specific errors

## Best Practices

1. **Backup your code** before running --write-docs
2. **Review generated docstrings** - AI-generated content should be verified
3. **Run on small batches** first to test the output quality
4. **Use version control** to easily revert changes if needed
5. **Set reasonable expectations** - generated docstrings may need manual refinement

## Integration with CI/CD

You can integrate this into your CI/CD pipeline:

```bash
# Check documentation coverage without modifying files
python scanner.py --format json --output coverage.json

# Generate missing docs (in a separate branch)
python scanner.py --write-docs
```

## Support

For issues or questions:
- Check the main README.md
- Review the implementation in `writers/` and `core/doc_generator.py`
- Ensure your watsonx.ai credentials are valid