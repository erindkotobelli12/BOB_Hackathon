"""Markdown output formatter for scan results."""

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class MarkdownFormatter:
    """Formats scan results as human-readable Markdown documentation."""
    
    @staticmethod
    def format(
        files_data: List[Dict[str, Any]],
        root_directory: str,
        coverage_report: Dict[str, Any]
    ) -> str:
        """
        Format scan results as Markdown documentation.
        
        Args:
            files_data: List of file metadata dictionaries
            root_directory: Root directory that was scanned
            coverage_report: Documentation coverage report
            
        Returns:
            Formatted markdown string
        """
        lines = []
        
        # Header
        project_name = Path(root_directory).name
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        
        lines.append(f"# 📚 Documentation Report: {project_name}")
        lines.append("")
        lines.append(f"**Generated:** {timestamp}")
        lines.append(f"**Root Directory:** `{root_directory}`")
        lines.append("")
        
        # Coverage Summary Table
        lines.append("## 📊 Coverage Summary")
        lines.append("")
        lines.append("| Language | Files | Functions | Coverage % |")
        lines.append("|----------|-------|-----------|------------|")
        
        # Calculate per-language statistics
        language_stats = MarkdownFormatter._calculate_language_stats(files_data)
        
        for lang, stats in sorted(language_stats.items()):
            coverage_pct = coverage_report['by_language'].get(lang, 0.0)
            lines.append(
                f"| {lang} | {stats['files']} | {stats['functions']} | {coverage_pct:.1f}% |"
            )
        
        # Overall totals
        total_files = len(files_data)
        total_functions = sum(stats['functions'] for stats in language_stats.values())
        overall_coverage = coverage_report['overall_coverage']
        
        lines.append(f"| **Total** | **{total_files}** | **{total_functions}** | **{overall_coverage:.1f}%** |")
        lines.append("")
        
        # Undocumented Items Section
        undocumented = coverage_report.get('undocumented_items', [])
        
        if undocumented:
            lines.append("## ⚠️ Undocumented Items")
            lines.append("")
            lines.append(f"Found **{len(undocumented)}** undocumented functions/methods:")
            lines.append("")
            
            # Group by file
            items_by_file = {}
            for item in undocumented:
                file_path = item['file']
                if file_path not in items_by_file:
                    items_by_file[file_path] = []
                items_by_file[file_path].append(item)
            
            for file_path in sorted(items_by_file.keys()):
                lines.append(f"### `{file_path}`")
                lines.append("")
                
                for item in sorted(items_by_file[file_path], key=lambda x: x['line']):
                    item_type = item['type']
                    item_name = item['name']
                    line_num = item['line']
                    lines.append(f"- **{item_name}** ({item_type}) - Line {line_num}")
                
                lines.append("")
        else:
            lines.append("## ✅ All Items Documented")
            lines.append("")
            lines.append("Congratulations! All functions and methods have documentation.")
            lines.append("")
        
        # File Documentation Section
        lines.append("## 📄 File Documentation")
        lines.append("")
        
        for file_data in sorted(files_data, key=lambda x: x.get('path', '')):
            file_path = file_data.get('path', 'unknown')
            language = file_data.get('language', 'unknown')
            
            lines.append(f"### `{file_path}`")
            lines.append("")
            lines.append(f"**Language:** {language}")
            lines.append("")
            
            # Functions
            functions = file_data.get('functions', [])
            if functions:
                lines.append("#### Functions")
                lines.append("")
                
                for func in sorted(functions, key=lambda x: x.get('line_start', 0)):
                    lines.extend(MarkdownFormatter._format_function(func))
            
            # Classes
            classes = file_data.get('classes', [])
            if classes:
                lines.append("#### Classes")
                lines.append("")
                
                for cls in sorted(classes, key=lambda x: x.get('line_start', 0)):
                    lines.extend(MarkdownFormatter._format_class(cls))
            
            # If no functions or classes
            if not functions and not classes:
                lines.append("_No functions or classes found._")
                lines.append("")
            
            lines.append("---")
            lines.append("")
        
        # Footer with stats
        lines.append("## 📈 Summary Statistics")
        lines.append("")
        lines.append(f"- **Total Files Scanned:** {total_files}")
        lines.append(f"- **Total Functions/Methods:** {total_functions}")
        lines.append(f"- **Total Classes:** {sum(len(f.get('classes', [])) for f in files_data)}")
        lines.append(f"- **Documentation Coverage:** {overall_coverage:.1f}%")
        lines.append(f"- **Documented Items:** {coverage_report['documented_items']}")
        lines.append(f"- **Undocumented Items:** {coverage_report['undocumented_items_count']}")
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("_Generated by Codebase Scanner_")
        
        return '\n'.join(lines)
    
    @staticmethod
    def _calculate_language_stats(files_data: List[Dict[str, Any]]) -> Dict[str, Dict[str, int]]:
        """
        Calculate statistics per language.
        
        Args:
            files_data: List of file metadata dictionaries
            
        Returns:
            Dictionary mapping language to stats
        """
        stats = {}
        
        for file_data in files_data:
            language = file_data.get('language', 'unknown')
            
            if language not in stats:
                stats[language] = {'files': 0, 'functions': 0}
            
            stats[language]['files'] += 1
            
            # Count functions
            stats[language]['functions'] += len(file_data.get('functions', []))
            
            # Count methods in classes
            for cls in file_data.get('classes', []):
                stats[language]['functions'] += len(cls.get('methods', []))
        
        return stats
    
    @staticmethod
    def _format_function(func: Dict[str, Any]) -> List[str]:
        """
        Format a function as markdown.
        
        Args:
            func: Function metadata dictionary
            
        Returns:
            List of markdown lines
        """
        lines = []
        
        name = func.get('name', 'unknown')
        params = func.get('parameters', [])
        return_type = func.get('return_type', 'unknown')
        docstring = (func.get('docstring') or '').strip()
        line_start = func.get('line_start', 0)
        
        # Function signature
        param_names = [p.get('name', '') if isinstance(p, dict) else str(p) for p in params]
        param_str = ', '.join(param_names) if param_names else ''
        lines.append(f"##### `{name}({param_str})`")
        lines.append("")
        lines.append(f"**Line:** {line_start} | **Returns:** `{return_type}`")
        lines.append("")
        
        # Parameters
        if params:
            lines.append("**Parameters:**")
            for param in params:
                if isinstance(param, dict):
                    param_name = param.get('name', 'unknown')
                    param_type = param.get('type', '')
                    if param_type:
                        lines.append(f"- `{param_name}` ({param_type})")
                    else:
                        lines.append(f"- `{param_name}`")
                else:
                    lines.append(f"- `{param}`")
            lines.append("")
        
        # Docstring
        if docstring:
            lines.append("**Documentation:**")
            lines.append("")
            # Indent docstring
            for doc_line in docstring.split('\n'):
                lines.append(f"> {doc_line}")
            lines.append("")
        else:
            lines.append("**Documentation:** _No documentation_")
            lines.append("")
        
        return lines
    
    @staticmethod
    def _format_class(cls: Dict[str, Any]) -> List[str]:
        """
        Format a class as markdown.
        
        Args:
            cls: Class metadata dictionary
            
        Returns:
            List of markdown lines
        """
        lines = []
        
        name = cls.get('name', 'unknown')
        docstring = (cls.get('docstring') or '').strip()
        line_start = cls.get('line_start', 0)
        methods = cls.get('methods', [])
        
        # Class header
        lines.append(f"##### Class: `{name}`")
        lines.append("")
        lines.append(f"**Line:** {line_start}")
        lines.append("")
        
        # Class docstring
        if docstring:
            lines.append("**Documentation:**")
            lines.append("")
            for doc_line in docstring.split('\n'):
                lines.append(f"> {doc_line}")
            lines.append("")
        else:
            lines.append("**Documentation:** _No documentation_")
            lines.append("")
        
        # Methods
        if methods:
            lines.append("**Methods:**")
            lines.append("")
            
            for method in sorted(methods, key=lambda x: x.get('line_start', 0)):
                method_name = method.get('name', 'unknown')
                method_params = method.get('parameters', [])
                method_return = method.get('return_type', 'unknown')
                method_docstring = (method.get('docstring') or '').strip()
                method_line = method.get('line_start', 0)
                
                method_param_names = [p.get('name', '') if isinstance(p, dict) else str(p) for p in method_params]
                param_str = ', '.join(method_param_names) if method_param_names else ''
                lines.append(f"- **`{method_name}({param_str})`** (Line {method_line})")
                lines.append(f"  - Returns: `{method_return}`")
                
                if method_docstring:
                    # Show first line of docstring
                    first_line = method_docstring.split('\n')[0]
                    lines.append(f"  - {first_line}")
                else:
                    lines.append(f"  - _No documentation_")
                
                lines.append("")
        
        return lines
    
    @staticmethod
    def save(content: str, output_path: Path) -> None:
        """
        Save formatted markdown content to file.
        
        Args:
            content: Markdown content string
            output_path: Path to output file
        """
        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)


# Made with Bob