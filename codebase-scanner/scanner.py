"""Main scanner script for codebase documentation extraction."""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any

from core.walker import DirectoryWalker
from core.extractor import MetadataExtractor
from formatters.json_formatter import JSONFormatter
from utils.logger import setup_logger, log_scan_summary


def load_config(config_path: Path) -> Dict[str, Any]:
    """
    Load configuration from JSON file.
    
    Args:
        config_path: Path to config file
        
    Returns:
        Configuration dictionary
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error loading config file: {e}")
        sys.exit(1)


def scan_codebase(config: Dict[str, Any]) -> None:
    """
    Scan codebase and generate documentation metadata.
    
    Args:
        config: Configuration dictionary
    """
    # Setup logger
    logger = setup_logger(
        verbose=config.get('verbose_logging', True),
        log_file=config.get('log_file')
    )
    
    logger.info("Starting codebase scan")
    logger.info(f"Root directory: {config['root_directory']}")
    
    # Initialize components
    root_dir = Path(config['root_directory']).resolve()
    walker = DirectoryWalker(
        root_dir=root_dir,
        exclude_patterns=config.get('exclude_patterns', []),
        include_extensions=config.get('include_extensions', []),
        max_file_size_mb=config.get('max_file_size_mb', 10.0),
        follow_symlinks=config.get('follow_symlinks', False),
        logger=logger
    )
    
    extractor = MetadataExtractor(logger=logger)
    
    # Scan files
    logger.info("Walking directory tree...")
    files_data = []
    
    for file_path in walker.walk():
        logger.debug(f"Processing: {file_path}")
        metadata = extractor.extract(file_path)
        files_data.append(metadata)
    
    # Calculate coverage report
    logger.info("Calculating documentation coverage...")
    coverage_report = JSONFormatter.calculate_coverage_report(files_data)
    
    # Format output
    logger.info("Formatting output...")
    output_data = JSONFormatter.format(
        files_data=files_data,
        root_directory=str(root_dir),
        coverage_report=coverage_report
    )
    
    # Save to file
    output_path = Path(config.get('output_file', 'output/documentation.json'))
    logger.info(f"Saving results to: {output_path}")
    JSONFormatter.save(output_data, output_path)
    
    # Log summary
    stats = {
        'total_files': len(files_data),
        'total_functions': output_data['scan_metadata']['total_functions'],
        'total_classes': output_data['scan_metadata']['total_classes'],
        'languages_detected': output_data['scan_metadata']['languages_detected'],
        'overall_coverage': coverage_report['overall_coverage'],
    }
    log_scan_summary(logger, stats)
    
    logger.info(f"Scan complete! Results saved to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Scan codebase and extract documentation metadata',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Use default config file
  python scanner.py
  
  # Specify custom config
  python scanner.py --config my-config.json
  
  # Override root directory
  python scanner.py --root /path/to/project
  
  # Override output file
  python scanner.py --output results.json
  
  # Specify languages to scan
  python scanner.py --languages python,javascript
        """
    )
    
    parser.add_argument(
        '--config',
        type=str,
        default='config.json',
        help='Path to configuration file (default: config.json)'
    )
    
    parser.add_argument(
        '--root',
        type=str,
        help='Root directory to scan (overrides config)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        help='Output file path (overrides config)'
    )
    
    parser.add_argument(
        '--languages',
        type=str,
        help='Comma-separated list of languages to scan (e.g., python,javascript)'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Load configuration
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"Error: Config file not found: {config_path}")
        print("Creating default config file...")
        
        # Create default config
        default_config = {
            "root_directory": ".",
            "output_file": "output/documentation.json",
            "exclude_patterns": [
                "node_modules/**",
                "venv/**",
                "__pycache__/**",
                ".git/**"
            ],
            "include_extensions": [
                ".py", ".js", ".ts", ".jsx", ".tsx",
                ".java", ".c", ".cpp", ".h", ".hpp"
            ],
            "max_file_size_mb": 10,
            "follow_symlinks": False,
            "extract_imports": True,
            "calculate_coverage": True,
            "verbose_logging": True
        }
        
        config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2)
        
        print(f"Created default config at: {config_path}")
        config = default_config
    else:
        config = load_config(config_path)
    
    # Apply command line overrides
    if args.root:
        config['root_directory'] = args.root
    
    if args.output:
        config['output_file'] = args.output
    
    if args.verbose:
        config['verbose_logging'] = True
    
    if args.languages:
        # Filter extensions based on specified languages
        language_extensions = {
            'python': ['.py'],
            'javascript': ['.js', '.jsx'],
            'typescript': ['.ts', '.tsx'],
            'java': ['.java'],
            'c': ['.c', '.h'],
            'cpp': ['.cpp', '.cc', '.cxx', '.hpp', '.hh', '.hxx'],
        }
        
        languages = [lang.strip() for lang in args.languages.split(',')]
        extensions = []
        for lang in languages:
            extensions.extend(language_extensions.get(lang, []))
        
        if extensions:
            config['include_extensions'] = extensions
    
    # Validate root directory
    root_path = Path(config['root_directory'])
    if not root_path.exists():
        print(f"Error: Root directory does not exist: {root_path}")
        sys.exit(1)
    
    if not root_path.is_dir():
        print(f"Error: Root path is not a directory: {root_path}")
        sys.exit(1)
    
    # Run scan
    try:
        scan_codebase(config)
    except KeyboardInterrupt:
        print("\nScan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Error during scan: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

# Made with Bob
