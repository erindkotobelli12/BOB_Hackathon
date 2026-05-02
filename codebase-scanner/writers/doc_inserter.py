"""Insert docstrings into Python source files using AST."""

import ast
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class DocInserter:
    """Insert generated docstrings into Python source files."""
    
    def __init__(self, file_path: Path):
        """Initialize doc inserter for a specific file."""
        self.file_path = file_path
        self.lines: List[str] = []
        self.modified = False
    
    def insert_docstrings(self, docstrings: Dict[str, str]) -> bool:
        """
        Insert docstrings into the file.
        
        Args:
            docstrings: Dict mapping function/method names to docstring content
            
        Returns:
            True if file was modified, False otherwise
        """
        if not docstrings:
            return False
        
        # Read file
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()
        
        # Parse AST
        try:
            tree = ast.parse(''.join(self.lines), filename=str(self.file_path))
        except SyntaxError:
            print(f"Syntax error in {self.file_path}, skipping")
            return False
        
        # Collect insertion points
        insertions = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if node.name in docstrings and not ast.get_docstring(node):
                    insertions.append((node.lineno, node.name, docstrings[node.name]))
            elif isinstance(node, ast.ClassDef):
                if node.name in docstrings and not ast.get_docstring(node):
                    insertions.append((node.lineno, node.name, docstrings[node.name]))
        
        if not insertions:
            return False
        
        # Sort by line number in reverse to insert from bottom to top
        insertions.sort(reverse=True)
        
        # Insert docstrings
        for line_num, name, docstring in insertions:
            self._insert_at_line(line_num, docstring)
            self.modified = True
        
        # Write back to file
        if self.modified:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                f.writelines(self.lines)
        
        return self.modified
    
    def _insert_at_line(self, line_num: int, docstring: str) -> None:
        """Insert docstring after the function/class definition line."""
        # line_num is 1-based, convert to 0-based index
        idx = line_num - 1
        
        # Find the line with the colon (could be multi-line signature)
        while idx < len(self.lines) and ':' not in self.lines[idx]:
            idx += 1
        
        if idx >= len(self.lines):
            return
        
        # Get indentation from next line or use default
        indent = self._get_indent(idx + 1)
        
        # Format docstring
        formatted = self._format_docstring(docstring, indent)
        
        # Insert after the definition line
        self.lines.insert(idx + 1, formatted)
    
    def _get_indent(self, line_idx: int) -> str:
        """Get indentation from a line."""
        if line_idx >= len(self.lines):
            return '    '
        
        line = self.lines[line_idx]
        indent = ''
        for char in line:
            if char in (' ', '\t'):
                indent += char
            else:
                break
        
        return indent if indent else '    '
    
    def _format_docstring(self, docstring: str, indent: str) -> str:
        """Format docstring with proper indentation and quotes.
        
        Follows Google style: first line on same line as opening quotes.
        """
        lines = docstring.split('\n')
        
        if not lines:
            return f'{indent}""""""\n'
        
        # Build formatted docstring with first line on same line as opening quotes
        result = f'{indent}"""{lines[0]}\n'
        
        # Add remaining lines
        for line in lines[1:]:
            if line.strip():
                result += f'{indent}{line}\n'
            else:
                result += '\n'
        
        result += f'{indent}"""\n'
        
        return result


def insert_docstrings_batch(file_docstrings: Dict[Path, Dict[str, str]]) -> Dict[Path, bool]:
    """
    Insert docstrings into multiple files.
    
    Args:
        file_docstrings: Dict mapping file paths to docstring dicts
        
    Returns:
        Dict mapping file paths to success status
    """
    results = {}
    for file_path, docstrings in file_docstrings.items():
        inserter = DocInserter(file_path)
        results[file_path] = inserter.insert_docstrings(docstrings)
    return results

# Made with Bob
