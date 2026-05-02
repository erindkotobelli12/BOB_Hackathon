"""Documentation generator orchestrator for the --write-docs feature."""

import logging
from pathlib import Path
from typing import Dict, List, Any
from writers.python_writer import generate_docstrings_for_files
from writers.doc_inserter import insert_docstrings_batch


class DocumentationGenerator:
    """Orchestrate documentation generation and insertion."""
    
    def __init__(self, logger: logging.Logger | None = None, dry_run: bool = False):
        """Initialize documentation generator."""
        self.logger = logger or logging.getLogger(__name__)
        self.dry_run = dry_run
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'functions_documented': 0,
            'classes_documented': 0,
            'methods_documented': 0,
            'errors': 0
        }
    
    def generate_and_write(self, files_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generate docstrings and write them to files.
        
        Args:
            files_data: List of file metadata from scanner
            
        Returns:
            Statistics about the documentation generation
        """
        mode = "DRY RUN" if self.dry_run else "documentation generation"
        self.logger.info(f"Starting {mode}...")
        
        # Filter Python files only
        python_files = [f for f in files_data if f.get('language') == 'python']
        self.logger.info(f"Found {len(python_files)} Python files to process")
        
        if not python_files:
            self.logger.warning("No Python files found to document")
            return self.stats
        
        # Generate docstrings
        if self.dry_run:
            self.logger.info("DRY RUN: Identifying undocumented functions...")
        else:
            self.logger.info("Generating docstrings using watsonx.ai...")
        
        try:
            file_docstrings = generate_docstrings_for_files(python_files, dry_run=self.dry_run)
        except Exception as e:
            self.logger.error(f"Error generating docstrings: {e}")
            self.stats['errors'] += 1
            return self.stats
        
        if not file_docstrings:
            self.logger.info("No undocumented functions found")
            return self.stats
        
        # Count items to document
        total_items = sum(len(docs) for docs in file_docstrings.values())
        
        if self.dry_run:
            self.logger.info(f"DRY RUN: Would document {total_items} items in {len(file_docstrings)} files")
            self._print_dry_run_report(file_docstrings, python_files)
            return self.stats
        
        self.logger.info(f"Generated {total_items} docstrings for {len(file_docstrings)} files")
        
        # Insert docstrings into files
        self.logger.info("Inserting docstrings into source files...")
        try:
            results = insert_docstrings_batch(file_docstrings)
        except Exception as e:
            self.logger.error(f"Error inserting docstrings: {e}")
            self.stats['errors'] += 1
            return self.stats
        
        # Update statistics
        self._update_stats(file_docstrings, results, python_files)
        
        # Print progress report
        self._print_report()
        
        return self.stats
    
    def _update_stats(self, file_docstrings: Dict[Path, Dict[str, str]], 
                     results: Dict[Path, bool], 
                     files_data: List[Dict[str, Any]]) -> None:
        """Update statistics based on results."""
        self.stats['files_processed'] = len(files_data)
        self.stats['files_modified'] = sum(1 for success in results.values() if success)
        
        # Count documented items by type
        for file_path, docstrings in file_docstrings.items():
            # Find corresponding file data
            file_data = next((f for f in files_data if Path(f['path']) == file_path), None)
            if not file_data:
                continue
            
            for name in docstrings.keys():
                # Check if it's a function
                if any(f['name'] == name for f in file_data.get('functions', [])):
                    self.stats['functions_documented'] += 1
                # Check if it's a class
                elif any(c['name'] == name for c in file_data.get('classes', [])):
                    self.stats['classes_documented'] += 1
                # Otherwise it's a method
                else:
                    self.stats['methods_documented'] += 1
    
    def _print_report(self) -> None:
        """Print progress report."""
        print("\n" + "="*60)
        print("Documentation Generation Report")
        print("="*60)
        print(f"Files processed:       {self.stats['files_processed']}")
        print(f"Files modified:        {self.stats['files_modified']}")
        print(f"Functions documented:  {self.stats['functions_documented']}")
        print(f"Classes documented:    {self.stats['classes_documented']}")
        print(f"Methods documented:    {self.stats['methods_documented']}")
        
        total_documented = (self.stats['functions_documented'] + 
                          self.stats['classes_documented'] + 
                          self.stats['methods_documented'])
        print(f"Total items documented: {total_documented}")
        
        if self.stats['errors'] > 0:
            print(f"Errors encountered:    {self.stats['errors']}")
        
        print("="*60 + "\n")
    
    def _print_dry_run_report(self, file_docstrings: Dict[Path, Dict[str, str]],
                              files_data: List[Dict[str, Any]]) -> None:
        """Print dry run report showing what would be documented."""
        print("\n" + "="*60)
        print("DRY RUN: Documentation Preview")
        print("="*60)
        
        for file_path, docstrings in file_docstrings.items():
            print(f"\n{file_path}:")
            for name in docstrings.keys():
                print(f"  - {name}")
        
        total_items = sum(len(docs) for docs in file_docstrings.values())
        print(f"\nTotal items that would be documented: {total_items}")
        print(f"Files that would be modified: {len(file_docstrings)}")
        print("\nTo actually generate documentation, run without --dry-run")
        print("="*60 + "\n")


def generate_documentation(files_data: List[Dict[str, Any]],
                          logger: logging.Logger | None = None,
                          dry_run: bool = False) -> Dict[str, Any]:
    """
    Generate documentation for scanned files.
    
    Args:
        files_data: List of file metadata from scanner
        logger: Optional logger instance
        dry_run: If True, only show what would be documented
        
    Returns:
        Statistics dictionary
    """
    generator = DocumentationGenerator(logger, dry_run=dry_run)
    return generator.generate_and_write(files_data)

# Made with Bob
