# Demo Script Plan: demo.py

## Overview
Create an impressive, single-command demo script that showcases the codebase scanner's capabilities by analyzing a real-world open-source repository.

## Script Specification

### File: `demo.py`
**Location**: `codebase-scanner/demo.py`

### Purpose
Demonstrate the scanner's power by:
1. Cloning a well-known public GitHub repository
2. Running the scanner to analyze documentation coverage
3. Displaying impressive, formatted statistics
4. Showing top 10 undocumented functions
5. Optionally generating documentation with `--write-docs`

### Command Usage
```bash
# Basic demo - scan and report
python demo.py

# Demo with documentation generation
python demo.py --write-docs

# Choose different repository
python demo.py --repo flask/flask

# Clean up after demo
python demo.py --cleanup
```

## Implementation Details

### 1. Repository Options
**Default**: `requests/requests` (popular, well-documented baseline)

**Alternative Options**:
- `flask/flask` - Web framework
- `django/django` - Large framework
- `scikit-learn/scikit-learn` - ML library
- `pandas-dev/pandas` - Data analysis
- `psf/black` - Code formatter

**Selection Criteria**:
- Popular and recognizable
- Python-based
- Mix of documented and undocumented code
- Reasonable size (not too large for demo)

### 2. Script Flow

```python
#!/usr/bin/env python3
"""
Impressive demo of the codebase scanner.

This script clones a popular open-source repository and demonstrates
the scanner's documentation analysis capabilities.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

# ANSI color codes for impressive output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_banner():
    """Print impressive ASCII banner"""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        🔍 CODEBASE DOCUMENTATION SCANNER DEMO 🔍              ║
║                                                               ║
║     Analyzing Real-World Open Source Repositories            ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
{Colors.END}
    """
    print(banner)

def clone_repository(repo_url: str, target_dir: Path) -> bool:
    """Clone GitHub repository to target directory"""
    print(f"\n{Colors.BLUE}📥 Cloning repository: {repo_url}{Colors.END}")
    print(f"   Target: {target_dir}")
    
    try:
        subprocess.run(
            ['git', 'clone', '--depth', '1', repo_url, str(target_dir)],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"{Colors.GREEN}✓ Repository cloned successfully{Colors.END}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}✗ Failed to clone repository: {e}{Colors.END}")
        return False

def run_scanner(repo_dir: Path, output_file: Path) -> Dict[str, Any]:
    """Run the codebase scanner on the repository"""
    print(f"\n{Colors.BLUE}🔍 Scanning repository...{Colors.END}")
    
    # Create config for this scan
    config = {
        "root_directory": str(repo_dir),
        "output_file": str(output_file),
        "exclude_patterns": [
            "node_modules/**",
            "venv/**",
            "env/**",
            "__pycache__/**",
            ".git/**",
            "*.pyc",
            "tests/**",
            "test/**",
            "docs/**",
            "examples/**"
        ],
        "include_extensions": [".py"],
        "max_file_size_mb": 10,
        "follow_symlinks": False,
        "extract_imports": True,
        "calculate_coverage": True,
        "verbose_logging": False
    }
    
    config_path = repo_dir / 'scan_config.json'
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    # Run scanner
    try:
        subprocess.run(
            [sys.executable, 'scanner.py', '--config', str(config_path)],
            check=True,
            capture_output=True,
            text=True
        )
        
        # Load results
        with open(output_file, 'r') as f:
            results = json.load(f)
        
        print(f"{Colors.GREEN}✓ Scan complete{Colors.END}")
        return results
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}✗ Scan failed: {e}{Colors.END}")
        return {}

def print_statistics(results: Dict[str, Any]):
    """Print impressive formatted statistics"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}📊 DOCUMENTATION ANALYSIS RESULTS{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}\n")
    
    metadata = results.get('scan_metadata', {})
    coverage = results.get('coverage_report', {})
    
    # Overall statistics
    print(f"{Colors.BOLD}Repository Statistics:{Colors.END}")
    print(f"  📁 Total Files Scanned:     {Colors.YELLOW}{metadata.get('total_files', 0):>6}{Colors.END}")
    print(f"  📝 Total Functions:         {Colors.YELLOW}{metadata.get('total_functions', 0):>6}{Colors.END}")
    print(f"  🏛️  Total Classes:           {Colors.YELLOW}{metadata.get('total_classes', 0):>6}{Colors.END}")
    print(f"  📦 Total Methods:           {Colors.YELLOW}{metadata.get('total_methods', 0):>6}{Colors.END}")
    
    # Coverage statistics
    overall_coverage = coverage.get('overall_coverage', 0)
    coverage_color = Colors.GREEN if overall_coverage >= 80 else Colors.YELLOW if overall_coverage >= 50 else Colors.RED
    
    print(f"\n{Colors.BOLD}Documentation Coverage:{Colors.END}")
    print(f"  📈 Overall Coverage:        {coverage_color}{overall_coverage:>5.1f}%{Colors.END}")
    print(f"  ✅ Documented Items:        {Colors.GREEN}{coverage.get('documented_items', 0):>6}{Colors.END}")
    print(f"  ❌ Undocumented Items:      {Colors.RED}{coverage.get('undocumented_items', 0):>6}{Colors.END}")
    
    # Language breakdown
    if 'by_language' in coverage:
        print(f"\n{Colors.BOLD}Coverage by Language:{Colors.END}")
        for lang, lang_coverage in coverage['by_language'].items():
            lang_pct = lang_coverage.get('coverage', 0)
            lang_color = Colors.GREEN if lang_pct >= 80 else Colors.YELLOW if lang_pct >= 50 else Colors.RED
            print(f"  {lang.capitalize():>12}: {lang_color}{lang_pct:>5.1f}%{Colors.END} "
                  f"({lang_coverage.get('documented', 0)}/{lang_coverage.get('total', 0)})")

def find_undocumented_items(results: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Find all undocumented functions and methods"""
    undocumented = []
    
    for file_data in results.get('files', []):
        file_path = file_data.get('file_path', '')
        
        # Check functions
        for func in file_data.get('functions', []):
            if not func.get('docstring'):
                undocumented.append({
                    'type': 'function',
                    'name': func['name'],
                    'file': file_path,
                    'line': func.get('line_start', 0),
                    'params': len(func.get('parameters', []))
                })
        
        # Check classes and methods
        for cls in file_data.get('classes', []):
            if not cls.get('docstring'):
                undocumented.append({
                    'type': 'class',
                    'name': cls['name'],
                    'file': file_path,
                    'line': cls.get('line_start', 0),
                    'methods': len(cls.get('methods', []))
                })
            
            for method in cls.get('methods', []):
                if not method.get('docstring'):
                    undocumented.append({
                        'type': 'method',
                        'name': f"{cls['name']}.{method['name']}",
                        'file': file_path,
                        'line': method.get('line_start', 0),
                        'params': len(method.get('parameters', []))
                    })
    
    return undocumented

def print_top_undocumented(undocumented: List[Dict[str, Any]], limit: int = 10):
    """Print top undocumented items"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}🎯 TOP {limit} UNDOCUMENTED ITEMS{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}\n")
    
    if not undocumented:
        print(f"{Colors.GREEN}🎉 All items are documented! Excellent work!{Colors.END}")
        return
    
    # Sort by complexity (number of parameters/methods)
    sorted_items = sorted(
        undocumented[:limit],
        key=lambda x: x.get('params', x.get('methods', 0)),
        reverse=True
    )
    
    for i, item in enumerate(sorted_items, 1):
        type_icon = {'function': '📝', 'class': '🏛️', 'method': '⚙️'}.get(item['type'], '📄')
        complexity = item.get('params', item.get('methods', 0))
        
        print(f"{Colors.BOLD}{i:2d}. {type_icon} {item['name']}{Colors.END}")
        print(f"     Type: {item['type'].capitalize()}")
        print(f"     File: {Colors.CYAN}{item['file']}{Colors.END}:{item['line']}")
        print(f"     Complexity: {complexity} {'parameters' if 'params' in item else 'methods'}")
        print()

def print_summary(results: Dict[str, Any], undocumented: List[Dict[str, Any]]):
    """Print final summary with recommendations"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}📋 SUMMARY & RECOMMENDATIONS{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}\n")
    
    coverage = results.get('coverage_report', {}).get('overall_coverage', 0)
    total_undocumented = len(undocumented)
    
    if coverage >= 80:
        print(f"{Colors.GREEN}✅ Excellent documentation coverage! ({coverage:.1f}%){Colors.END}")
        print(f"   This repository maintains high documentation standards.")
    elif coverage >= 50:
        print(f"{Colors.YELLOW}⚠️  Moderate documentation coverage ({coverage:.1f}%){Colors.END}")
        print(f"   Consider documenting the {total_undocumented} undocumented items.")
    else:
        print(f"{Colors.RED}❌ Low documentation coverage ({coverage:.1f}%){Colors.END}")
        print(f"   {total_undocumented} items need documentation.")
    
    print(f"\n{Colors.BOLD}To generate documentation automatically:{Colors.END}")
    print(f"  {Colors.CYAN}python demo.py --write-docs{Colors.END}")
    print(f"\n{Colors.BOLD}To scan your own repository:{Colors.END}")
    print(f"  {Colors.CYAN}python scanner.py --root /path/to/your/repo{Colors.END}")

def run_write_docs(repo_dir: Path):
    """Run documentation generation"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}✍️  GENERATING DOCUMENTATION{Colors.END}")
    print(f"{Colors.CYAN}{Colors.BOLD}{'='*70}{Colors.END}\n")
    
    print(f"{Colors.YELLOW}⚠️  Note: --write-docs feature requires implementation{Colors.END}")
    print(f"   This would generate Google-style docstrings using watsonx.ai")
    print(f"   and insert them into the source files.\n")
    
    # TODO: Implement when --write-docs is ready
    # subprocess.run([sys.executable, 'scanner.py', '--root', str(repo_dir), '--write-docs'])

def main():
    """Main demo script"""
    parser = argparse.ArgumentParser(
        description='Demo the codebase scanner with real-world repositories',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python demo.py                          # Run demo with default repo
  python demo.py --write-docs             # Run demo and generate docs
  python demo.py --repo flask/flask       # Use different repository
  python demo.py --cleanup                # Clean up temp files
        """
    )
    
    parser.add_argument(
        '--repo',
        type=str,
        default='requests/requests',
        help='GitHub repository to analyze (format: owner/repo)'
    )
    
    parser.add_argument(
        '--write-docs',
        action='store_true',
        help='Generate documentation for undocumented items'
    )
    
    parser.add_argument(
        '--cleanup',
        action='store_true',
        help='Clean up temporary files and exit'
    )
    
    args = parser.parse_args()
    
    # Handle cleanup
    if args.cleanup:
        temp_dir = Path(tempfile.gettempdir()) / 'scanner_demo'
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
            print(f"{Colors.GREEN}✓ Cleaned up temporary files{Colors.END}")
        return
    
    # Print banner
    print_banner()
    
    # Setup
    temp_dir = Path(tempfile.gettempdir()) / 'scanner_demo'
    repo_dir = temp_dir / args.repo.split('/')[-1]
    output_file = temp_dir / 'scan_results.json'
    
    # Create temp directory
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    # Clone repository
    repo_url = f"https://github.com/{args.repo}.git"
    if not clone_repository(repo_url, repo_dir):
        return 1
    
    # Run scanner
    results = run_scanner(repo_dir, output_file)
    if not results:
        return 1
    
    # Display results
    print_statistics(results)
    
    # Find and display undocumented items
    undocumented = find_undocumented_items(results)
    print_top_undocumented(undocumented, limit=10)
    
    # Print summary
    print_summary(results, undocumented)
    
    # Run write-docs if requested
    if args.write_docs:
        run_write_docs(repo_dir)
    
    # Cleanup prompt
    print(f"\n{Colors.BOLD}Temporary files location:{Colors.END} {temp_dir}")
    print(f"{Colors.BOLD}To clean up:{Colors.END} python demo.py --cleanup\n")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
```

## Expected Output

### Basic Run
```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        🔍 CODEBASE DOCUMENTATION SCANNER DEMO 🔍              ║
║                                                               ║
║     Analyzing Real-World Open Source Repositories            ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

📥 Cloning repository: https://github.com/requests/requests.git
   Target: /tmp/scanner_demo/requests
✓ Repository cloned successfully

🔍 Scanning repository...
✓ Scan complete

======================================================================
📊 DOCUMENTATION ANALYSIS RESULTS
======================================================================

Repository Statistics:
  📁 Total Files Scanned:         45
  📝 Total Functions:            234
  🏛️  Total Classes:              28
  📦 Total Methods:              156

Documentation Coverage:
  📈 Overall Coverage:          87.3%
  ✅ Documented Items:           365
  ❌ Undocumented Items:          53

Coverage by Language:
      Python:  87.3% (365/418)

======================================================================
🎯 TOP 10 UNDOCUMENTED ITEMS
======================================================================

 1. 📝 prepare_request
     Type: Function
     File: requests/sessions.py:412
     Complexity: 8 parameters

 2. 🏛️ HTTPAdapter
     Type: Class
     File: requests/adapters.py:89
     Complexity: 12 methods

 3. ⚙️ Session.request
     Type: Method
     File: requests/sessions.py:465
     Complexity: 11 parameters

...

======================================================================
📋 SUMMARY & RECOMMENDATIONS
======================================================================

✅ Excellent documentation coverage! (87.3%)
   This repository maintains high documentation standards.

To generate documentation automatically:
  python demo.py --write-docs

To scan your own repository:
  python scanner.py --root /path/to/your/repo

Temporary files location: /tmp/scanner_demo
To clean up: python demo.py --cleanup
```

## Features

### 1. Impressive Visual Output
- ANSI color codes for beautiful terminal output
- ASCII art banner
- Progress indicators
- Color-coded statistics (green/yellow/red based on coverage)

### 2. Real-World Analysis
- Clones actual open-source repositories
- Analyzes real code with real documentation patterns
- Shows meaningful statistics

### 3. Top 10 Undocumented Items
- Sorted by complexity (parameters/methods)
- Shows file location and line numbers
- Categorized by type (function/class/method)

### 4. Smart Recommendations
- Coverage-based feedback
- Actionable next steps
- Clear usage instructions

### 5. Easy Cleanup
- Uses temp directory
- Simple cleanup command
- No clutter in project directory

## Integration with --write-docs

When `--write-docs` is implemented, the demo will:
1. Show initial coverage
2. Generate documentation for undocumented items
3. Re-scan to show improvement
4. Display before/after comparison
5. Show sample generated docstrings

## Repository Selection Rationale

**Default: `requests/requests`**
- Very popular (50k+ stars)
- Well-known to Python developers
- Good documentation baseline (~85-90% coverage)
- Reasonable size for demo
- Mix of documented and undocumented code

**Alternatives**:
- `flask/flask` - Web framework, good coverage
- `scikit-learn/scikit-learn` - ML library, extensive docs
- `pandas-dev/pandas` - Data analysis, large codebase
- `psf/black` - Code formatter, smaller, focused

## Next Steps

1. Implement demo.py script
2. Test with multiple repositories
3. Refine output formatting
4. Add progress bars for long operations
5. Integrate with --write-docs when ready
6. Add option to save detailed report
7. Add comparison mode (before/after)