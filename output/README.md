# Output Directory

This directory contains generated scan results from the AI Documentation Agent.

## What Gets Generated

When you run the scanner, it creates:

### JSON Output (Structured Data)
- `<project>_scan.json` - Complete scan results with metadata
- Used by tools and automation
- Contains: functions, classes, parameters, docstrings, coverage metrics

### Markdown Output (Human-Readable)
- `<project>_scan.md` - Formatted documentation report
- Easy to read and share
- Contains: coverage summary, undocumented items list, statistics

## Files in This Directory

### Kept in Repository
- **`README.md`** (this file) - Documentation
- Files in `codebase-scanner/output/`:
  - `self_scan.json` (101KB) - Scanner scanning itself (demo)
  - `self_scan.md` (23KB) - Human-readable version
  - `documentation.md` (6KB) - Sample output

### Not in Repository (.gitignore)
Large scan results are excluded from git:
- `documentation.json` (865KB) - Too large
- `flask_scan.json` (429KB) - Can be regenerated
- `flask_scan.md` (121KB) - Can be regenerated
- Any `*_scan.json` or `*_scan.md` files

## Regenerating Output

To recreate scan results:

```bash
# Scan any project
cd codebase-scanner
python scanner.py --root /path/to/project --format both

# Scan Flask (from showcase)
python scanner.py --root $TEMP/flask/src --output ../output/flask_scan.json --format both

# Scan this project
python scanner.py --root .. --output ../output/documentation.json --format both
```

## Why Some Files Are Excluded

**Large JSON files (>100KB)** are excluded because:
- They can be regenerated in seconds
- They bloat the repository
- GitHub has file size limits
- They're project-specific, not reusable

**Small example files are kept** to show:
- What the output looks like
- How the scanner works on itself
- Demo for judges/users

## Output File Sizes

Typical sizes for reference:
- Small project (10 files): ~10-20KB JSON
- Medium project (100 files): ~100-200KB JSON
- Large project (1000 files): ~1-2MB JSON

**Recommendation**: Keep JSON files under 100KB in the repository.