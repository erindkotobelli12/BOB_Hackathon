# --write-docs Quick Start Guide

## Overview
This guide provides a quick reference for implementing and using the `--write-docs` feature for automatic Python documentation generation using watsonx.ai.

## Prerequisites

### 1. watsonx.ai Credentials
You need the following credentials from IBM watsonx.ai:
- API Key
- Project ID  
- API URL (e.g., `https://us-south.ml.cloud.ibm.com`)

### 2. Environment Setup
Create a `.env` file in the project root:
```bash
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_URL=https://us-south.ml.cloud.ibm.com
```

**Important**: Never commit `.env` to version control!

## Implementation Checklist

### Phase 1: Foundation (Day 1)
- [ ] Create `codebase-scanner/writers/` directory
- [ ] Create `writers/__init__.py`
- [ ] Create `.env.example` with template
- [ ] Update `.gitignore` to exclude `.env` and `*.bak`
- [ ] Implement `writers/base_writer.py` (abstract base class)

### Phase 2: API Integration (Day 2)
- [ ] Implement `writers/watsonx_client.py`
  - [ ] Load credentials from environment
  - [ ] Implement API request/response handling
  - [ ] Add retry logic with exponential backoff
  - [ ] Add error handling
- [ ] Test API connectivity with sample request

### Phase 3: Python Writer (Day 3)
- [ ] Implement `writers/python_writer.py`
  - [ ] Function docstring generation
  - [ ] Class docstring generation
  - [ ] Method docstring generation
  - [ ] Prompt engineering for watsonx.ai
- [ ] Test with sample functions from `demo/` directory

### Phase 4: File Operations (Day 4)
- [ ] Implement `writers/doc_inserter.py`
  - [ ] Backup creation (`.bak` files)
  - [ ] Safe insertion with indentation preservation
  - [ ] Python syntax validation
  - [ ] Automatic rollback on errors
- [ ] Test with sample files

### Phase 5: Orchestration (Day 5)
- [ ] Implement `core/doc_generator.py`
  - [ ] File filtering logic
  - [ ] Batch processing
  - [ ] Progress reporting
  - [ ] Error aggregation
- [ ] Test end-to-end workflow

### Phase 6: CLI Integration (Day 6)
- [ ] Modify `scanner.py`
  - [ ] Add `--write-docs` flag
  - [ ] Add `--dry-run` flag
  - [ ] Add `--no-backup` flag
  - [ ] Add `--min-coverage` flag
  - [ ] Add environment variable checks
  - [ ] Integrate documentation generation workflow
  - [ ] Add before/after comparison
- [ ] Test complete workflow

### Phase 7: Testing (Day 7)
- [ ] Create unit tests
  - [ ] `tests/test_watsonx_client.py`
  - [ ] `tests/test_python_writer.py`
  - [ ] `tests/test_doc_inserter.py`
  - [ ] `tests/test_doc_generator.py`
- [ ] Create integration tests
- [ ] Test with `demo/` directory files

## Usage Examples

### Basic Usage
```bash
# Set environment variables (one-time setup)
export WATSONX_API_KEY="your_key"
export WATSONX_PROJECT_ID="your_project_id"
export WATSONX_URL="https://us-south.ml.cloud.ibm.com"

# Scan and generate documentation
python scanner.py --write-docs

# Preview without modifying files
python scanner.py --write-docs --dry-run

# Target specific directory
python scanner.py --root ./demo --write-docs

# Target specific coverage threshold
python scanner.py --write-docs --min-coverage 90
```

### Advanced Usage
```bash
# Python files only
python scanner.py --languages python --write-docs

# Generate both JSON and Markdown reports
python scanner.py --write-docs --format both

# Skip backups (not recommended)
python scanner.py --write-docs --no-backup

# Combine with custom config
python scanner.py --config custom-config.json --write-docs
```

## File Structure

```
codebase-scanner/
├── .env                          # Your credentials (DO NOT COMMIT)
├── .env.example                  # Template for credentials
├── .gitignore                    # Updated to exclude .env and *.bak
├── scanner.py                    # Modified with --write-docs flag
├── config.json                   # Existing configuration
│
├── core/
│   ├── walker.py                 # Existing
│   ├── extractor.py              # Existing
│   ├── detector.py               # Existing
│   └── doc_generator.py          # NEW: Orchestrator
│
├── writers/                      # NEW: Documentation generation
│   ├── __init__.py
│   ├── base_writer.py           # Abstract base class
│   ├── watsonx_client.py        # API client
│   ├── python_writer.py         # Python-specific writer
│   └── doc_inserter.py          # File modification
│
├── parsers/                      # Existing
│   └── python_parser.py
│
├── tests/                        # Existing + new tests
│   ├── test_watsonx_client.py   # NEW
│   ├── test_python_writer.py    # NEW
│   ├── test_doc_inserter.py     # NEW
│   └── test_doc_generator.py    # NEW
│
└── demo/                         # Test files
    ├── utils.py
    ├── data_processor.py
    └── async_operations.py
```

## Key Components

### 1. WatsonxClient
**Purpose**: Handle watsonx.ai API interactions

**Key Methods**:
- `generate_docstring(signature, body, function_name)` - Generate docstring via API
- `_build_prompt(signature, body)` - Construct API prompt
- `_call_api(prompt)` - Make API request with retry logic

### 2. PythonDocumentationWriter
**Purpose**: Generate Google-style Python docstrings

**Key Methods**:
- `generate_function_doc(func_info, file_content)` - Generate function docstring
- `generate_class_doc(class_info, file_content)` - Generate class docstring
- `generate_method_doc(method_info, class_name, file_content)` - Generate method docstring

### 3. DocumentationInserter
**Purpose**: Safely modify source files

**Key Methods**:
- `insert_documentation(file_path, doc_items, create_backup)` - Insert docs into file
- `create_backup(file_path)` - Create `.bak` backup
- `validate_python_syntax(file_path)` - Validate syntax
- `restore_backup(backup_path, original_path)` - Rollback on error

### 4. DocumentationGenerator
**Purpose**: Orchestrate the entire process

**Key Methods**:
- `generate_documentation(scan_results, config)` - Main entry point
- `_process_file(file_data)` - Process single file
- `_filter_python_files(scan_results)` - Filter for Python files
- `_filter_undocumented(files)` - Filter for undocumented items

## Expected Output

### Successful Run
```
Starting codebase scan...
Root directory: /path/to/project
Walking directory tree...
Processing: demo/utils.py
Processing: demo/data_processor.py
Processing: demo/async_operations.py
Scan complete! Results saved to: output/documentation.json

============================================================
DOCUMENTATION GENERATION MODE
============================================================
Initial documentation coverage: 33.3%
Generating documentation for undocumented items...

Processing demo/utils.py...
  ✓ Documented 3 functions
Processing demo/data_processor.py...
  ✓ Documented 5 functions
Processing demo/async_operations.py...
  ✓ Documented 4 functions

Re-scanning to verify coverage improvements...

============================================================
DOCUMENTATION GENERATION COMPLETE
============================================================
Files modified: 3
Items documented: 12
Coverage before: 33.3%
Coverage after: 100.0%
Improvement: +66.7%

Detailed report saved to: output/documentation.md
```

### Dry Run
```
============================================================
DOCUMENTATION GENERATION MODE (DRY RUN)
============================================================
Initial documentation coverage: 33.3%

Would document the following items:

demo/utils.py:
  - format_timestamp (function, line 15)
  - parse_config (function, line 28)
  - validate_input (function, line 45)

demo/data_processor.py:
  - DataProcessor (class, line 10)
  - DataProcessor.process (method, line 25)
  - DataProcessor.validate (method, line 42)
  - load_data (function, line 60)
  - save_results (function, line 75)

demo/async_operations.py:
  - fetch_data (async function, line 12)
  - process_batch (async function, line 28)
  - AsyncProcessor (class, line 45)
  - AsyncProcessor.run (async method, line 55)

============================================================
DRY RUN COMPLETE (no files modified)
============================================================
Would document 12 items in 3 files
Estimated coverage after: 100.0%
```

## Error Messages

### Missing Credentials
```
Error: watsonx.ai credentials not found!
Please set the following environment variables:
  - WATSONX_API_KEY
  - WATSONX_PROJECT_ID
  - WATSONX_URL

See .env.example for details.
```

### API Error
```
Error: Failed to generate documentation for demo/utils.py:format_timestamp
Reason: API request failed after 3 retries
Skipping this item and continuing...
```

### Syntax Error
```
Error: Syntax error detected after inserting documentation in demo/utils.py
Restoring from backup...
File restored successfully. Please review the function manually.
```

## Testing Strategy

### Unit Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_python_writer.py

# Run with coverage
python -m pytest --cov=writers tests/
```

### Integration Test
```bash
# Test with demo directory
python scanner.py --root ./demo --write-docs --dry-run

# Actual run on demo
python scanner.py --root ./demo --write-docs
```

## Troubleshooting

### Issue: "API request failed"
**Solution**: Check your credentials and network connection
```bash
# Verify credentials are set
echo $WATSONX_API_KEY
echo $WATSONX_PROJECT_ID
echo $WATSONX_URL

# Test API connectivity
curl -X POST "$WATSONX_URL/ml/v1/text/generation" \
  -H "Authorization: Bearer $WATSONX_API_KEY" \
  -H "Content-Type: application/json"
```

### Issue: "Syntax error after insertion"
**Solution**: Check the backup file and review the generated docstring
```bash
# View backup
cat demo/utils.py.bak

# Compare with original
diff demo/utils.py.bak demo/utils.py
```

### Issue: "No items documented"
**Solution**: Verify files have undocumented functions
```bash
# Run scan first to see coverage
python scanner.py --root ./demo --format markdown

# Check the output
cat output/documentation.md
```

## Best Practices

1. **Always use --dry-run first** to preview changes
2. **Keep backups enabled** (default behavior)
3. **Test on a small directory first** before running on entire codebase
4. **Review generated documentation** for quality
5. **Commit changes incrementally** by directory or file type
6. **Set reasonable coverage targets** (80-90% is realistic)
7. **Use version control** before running --write-docs

## Next Steps

1. Review the implementation plan: [`WRITE_DOCS_PYTHON_IMPLEMENTATION.md`](WRITE_DOCS_PYTHON_IMPLEMENTATION.md)
2. Review the architecture: [`WRITE_DOCS_ARCHITECTURE.md`](WRITE_DOCS_ARCHITECTURE.md)
3. Switch to Code mode to begin implementation
4. Follow the implementation checklist above
5. Test thoroughly with demo/ directory
6. Deploy and monitor

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the detailed implementation plan
3. Check the architecture diagrams
4. Review the existing codebase documentation

## References

- [watsonx.ai API Documentation](https://cloud.ibm.com/apidocs/watsonx-ai)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [Python AST Documentation](https://docs.python.org/3/library/ast.html)