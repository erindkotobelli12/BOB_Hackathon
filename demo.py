#!/usr/bin/env python3
"""Demo script for codebase-scanner with --write-docs feature."""

import os
import sys
import subprocess
import json
import shutil
from pathlib import Path


def run_command(cmd, cwd=None):
    """Run a shell command and return output."""
    result = subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True
    )
    return result.returncode, result.stdout, result.stderr


def clone_flask():
    """Clone Flask repository if it doesn't exist."""
    flask_dir = Path("/tmp/flask")
    
    if flask_dir.exists():
        print(f"✓ Flask already cloned at {flask_dir}")
        return flask_dir
    
    print("Cloning Flask repository...")
    returncode, stdout, stderr = run_command(
        "git clone --depth 1 https://github.com/pallets/flask.git /tmp/flask"
    )
    
    if returncode != 0:
        print(f"Error cloning Flask: {stderr}")
        sys.exit(1)
    
    print(f"✓ Flask cloned to {flask_dir}")
    return flask_dir


def run_scanner(flask_dir):
    """Run scanner on Flask and return coverage report."""
    print("\n" + "="*60)
    print("Running codebase scanner on Flask...")
    print("="*60)
    
    scanner_dir = Path(__file__).parent / "codebase-scanner"
    output_file = scanner_dir / "output" / "flask_demo.json"
    
    cmd = f'python scanner.py --root "{flask_dir}" --output "{output_file}" --languages python'
    returncode, stdout, stderr = run_command(cmd, cwd=scanner_dir)
    
    if returncode != 0:
        print(f"Error running scanner: {stderr}")
        return None
    
    print(stdout)
    
    # Load and display coverage report
    if output_file.exists():
        with open(output_file, 'r') as f:
            data = json.load(f)
        
        coverage = data.get('coverage_report', {})
        print("\n" + "="*60)
        print("FLASK DOCUMENTATION COVERAGE REPORT")
        print("="*60)
        print(f"Overall Coverage: {coverage.get('overall_coverage', 0):.1f}%")
        print(f"Total Files: {data['scan_metadata'].get('total_files', 0)}")
        print(f"Total Functions: {data['scan_metadata'].get('total_functions', 0)}")
        print(f"Total Classes: {data['scan_metadata'].get('total_classes', 0)}")
        
        by_lang = coverage.get('by_language', {})
        if 'python' in by_lang:
            py_cov = by_lang['python']
            print(f"\nPython Coverage: {py_cov.get('coverage_percentage', 0):.1f}%")
            print(f"  Documented: {py_cov.get('documented', 0)}")
            print(f"  Undocumented: {py_cov.get('undocumented', 0)}")
        
        print("="*60)
        return data
    
    return None


def find_undocumented_functions(scan_data, limit=3):
    """Find undocumented functions from scan data."""
    undocumented = []
    
    for file_data in scan_data.get('files', []):
        if file_data.get('language') != 'python':
            continue
        
        for func in file_data.get('functions', []):
            if not func.get('docstring'):
                undocumented.append({
                    'file': file_data['path'],
                    'name': func['name'],
                    'line_start': func['line_start'],
                    'line_end': func.get('line_end', func['line_start'])
                })
                
                if len(undocumented) >= limit:
                    return undocumented
    
    return undocumented


def show_before_after(file_path, line_start, line_end):
    """Show before/after for a function."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Show context around the function
        start_idx = max(0, line_start - 2)
        end_idx = min(len(lines), line_end + 2)
        
        print("\n" + "-"*60)
        for i in range(start_idx, end_idx):
            print(f"{i+1:4d} | {lines[i]}", end='')
        print("-"*60)
    except Exception as e:
        print(f"Error reading file: {e}")


def demo_write_docs(flask_dir, scan_data):
    """Demonstrate --write-docs feature."""
    if not os.environ.get('WATSONX_API_KEY'):
        print("\n" + "="*60)
        print("WATSONX_API_KEY not set - skipping --write-docs demo")
        print("To see the --write-docs feature in action:")
        print("1. Copy .env.example to .env")
        print("2. Add your watsonx.ai credentials")
        print("3. Run this demo again")
        print("="*60)
        return
    
    print("\n" + "="*60)
    print("DEMONSTRATING --write-docs FEATURE")
    print("="*60)
    
    # Find 3 undocumented functions
    undoc_funcs = find_undocumented_functions(scan_data, limit=3)
    
    if not undoc_funcs:
        print("No undocumented functions found!")
        return
    
    print(f"\nFound {len(undoc_funcs)} undocumented functions:")
    for i, func in enumerate(undoc_funcs, 1):
        print(f"{i}. {func['name']} in {Path(func['file']).name}")
    
    # Show BEFORE state
    print("\n" + "="*60)
    print("BEFORE: Function without docstring")
    print("="*60)
    first_func = undoc_funcs[0]
    show_before_after(first_func['file'], first_func['line_start'], first_func['line_end'])
    
    # Run --write-docs on just this file
    print("\n" + "="*60)
    print("Running --write-docs...")
    print("="*60)
    
    scanner_dir = Path(__file__).parent / "codebase-scanner"
    file_to_doc = Path(first_func['file'])
    
    # Create a temp config for just this file
    temp_config = {
        "root_directory": str(file_to_doc.parent),
        "output_file": "output/temp_demo.json",
        "include_extensions": [".py"],
        "exclude_patterns": [],
        "verbose_logging": True
    }
    
    temp_config_path = scanner_dir / "temp_demo_config.json"
    with open(temp_config_path, 'w') as f:
        json.dump(temp_config, f)
    
    cmd = f'python scanner.py --config temp_demo_config.json --write-docs'
    returncode, stdout, stderr = run_command(cmd, cwd=scanner_dir)
    
    print(stdout)
    if stderr:
        print(f"Errors: {stderr}")
    
    # Clean up temp config
    temp_config_path.unlink(missing_ok=True)
    
    # Show AFTER state
    print("\n" + "="*60)
    print("AFTER: Function with AI-generated docstring")
    print("="*60)
    show_before_after(first_func['file'], first_func['line_start'], first_func['line_end'] + 10)
    
    print("\n" + "="*60)
    print("✓ Documentation generation complete!")
    print("="*60)


def main():
    """Main demo function."""
    print("="*60)
    print("CODEBASE SCANNER DEMO")
    print("="*60)
    
    # Step 1: Clone Flask
    flask_dir = clone_flask()
    
    # Step 2: Run scanner and show coverage
    scan_data = run_scanner(flask_dir)
    
    if not scan_data:
        print("Failed to scan Flask repository")
        sys.exit(1)
    
    # Step 3: Demo --write-docs if credentials available
    demo_write_docs(flask_dir, scan_data)
    
    print("\n" + "="*60)
    print("DEMO COMPLETE")
    print("="*60)
    print("\nTo try --write-docs yourself:")
    print("1. Set up your .env file with watsonx.ai credentials")
    print("2. Run: cd codebase-scanner && python scanner.py --write-docs")
    print("="*60)


if __name__ == '__main__':
    main()

# Made with Bob
