"""JSON output formatter for scan results."""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class JSONFormatter:
    """Formats scan results as JSON."""
    
    @staticmethod
    def format(
        files_data: List[Dict[str, Any]],
        root_directory: str,
        coverage_report: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Format scan results as structured JSON.
        
        Args:
            files_data: List of file metadata dictionaries
            root_directory: Root directory that was scanned
            coverage_report: Documentation coverage report
            
        Returns:
            Formatted dictionary ready for JSON serialization
        """
        # Calculate aggregate statistics
        total_functions = sum(len(f.get('functions', [])) for f in files_data)
        total_classes = sum(len(f.get('classes', [])) for f in files_data)
        
        # Get unique languages
        languages_detected = sorted(set(
            f.get('language', 'unknown') for f in files_data
        ))
        
        return {
            'scan_metadata': {
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'root_directory': root_directory,
                'total_files': len(files_data),
                'total_functions': total_functions,
                'total_classes': total_classes,
                'languages_detected': languages_detected,
            },
            'files': files_data,
            'coverage_report': coverage_report,
        }
    
    @staticmethod
    def save(data: Dict[str, Any], output_path: Path) -> None:
        """
        Save formatted data to JSON file.
        
        Args:
            data: Formatted data dictionary
            output_path: Path to output file
        """
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write JSON with pretty formatting
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    @staticmethod
    def calculate_coverage_report(files_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate documentation coverage report.
        
        Args:
            files_data: List of file metadata dictionaries
            
        Returns:
            Coverage report dictionary
        """
        # Overall statistics
        total_items = 0
        documented_items = 0
        
        # Per-language statistics
        language_stats: Dict[str, Dict[str, int]] = {}
        
        # Undocumented items
        undocumented_items = []
        
        for file_data in files_data:
            language = file_data.get('language', 'unknown')
            
            # Initialize language stats if needed
            if language not in language_stats:
                language_stats[language] = {
                    'total': 0,
                    'documented': 0,
                }
            
            # Count functions
            for func in file_data.get('functions', []):
                total_items += 1
                language_stats[language]['total'] += 1
                
                if func.get('docstring'):
                    documented_items += 1
                    language_stats[language]['documented'] += 1
                else:
                    undocumented_items.append({
                        'file': file_data.get('path', ''),
                        'type': 'function',
                        'name': func.get('name', ''),
                        'line': func.get('line_start', 0),
                    })
            
            # Count methods in classes
            for cls in file_data.get('classes', []):
                for method in cls.get('methods', []):
                    total_items += 1
                    language_stats[language]['total'] += 1
                    
                    if method.get('docstring'):
                        documented_items += 1
                        language_stats[language]['documented'] += 1
                    else:
                        undocumented_items.append({
                            'file': file_data.get('path', ''),
                            'type': 'method',
                            'name': f"{cls.get('name', '')}.{method.get('name', '')}",
                            'line': method.get('line_start', 0),
                        })
        
        # Calculate overall coverage
        overall_coverage = (documented_items / total_items * 100) if total_items > 0 else 100.0
        
        # Calculate per-language coverage
        by_language = {}
        for lang, stats in language_stats.items():
            coverage = (stats['documented'] / stats['total'] * 100) if stats['total'] > 0 else 100.0
            by_language[lang] = round(coverage, 2)
        
        return {
            'overall_coverage': round(overall_coverage, 2),
            'total_items': total_items,
            'documented_items': documented_items,
            'undocumented_items_count': len(undocumented_items),
            'by_language': by_language,
            'undocumented_items': undocumented_items[:100],  # Limit to first 100
        }

# Made with Bob
