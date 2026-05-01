# Output Directory

This directory contains the generated documentation files from the codebase scanner.

## Default Output

By default, the scanner generates:
- `documentation.json` - Complete scan results with metadata

## Output Format

The JSON file contains:
- **Scan Metadata**: Timestamp, file counts, languages detected
- **Files Array**: Detailed analysis of each file
  - Functions with parameters and return types
  - Classes with methods and inheritance
  - Documentation strings
  - Import statements
- **Coverage Report**: Documentation coverage statistics

## Example Output Structure

```json
{
  "scan_metadata": {
    "timestamp": "2026-05-01T15:00:00Z",
    "root_directory": "/path/to/project",
    "total_files": 150,
    "total_functions": 450,
    "total_classes": 120,
    "languages_detected": ["python", "javascript"]
  },
  "files": [...],
  "coverage_report": {
    "overall_coverage": 72.3,
    "by_language": {
      "python": 85.0,
      "javascript": 65.5
    }
  }
}
```

## Customizing Output

You can customize the output location in `config.json`:

```json
{
  "output_file": "output/my-custom-name.json"
}
```

Or via command line:

```bash
python scanner.py --output output/custom-results.json
```

## Using the Output

The generated JSON can be used for:
- Documentation generation tools
- Code analysis dashboards
- CI/CD quality gates
- IDE integrations
- Custom reporting scripts

## File Size

Output file size depends on codebase size:
- Small projects (< 100 files): ~100KB - 1MB
- Medium projects (100-1000 files): 1MB - 10MB
- Large projects (> 1000 files): 10MB+

## Cleanup

To clean old output files:

```bash
# Windows
del output\*.json

# Linux/Mac
rm output/*.json