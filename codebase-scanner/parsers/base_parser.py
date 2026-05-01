"""Base parser class for all language-specific parsers."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Any, Optional


class BaseParser(ABC):
    """Abstract base class for language parsers."""
    
    def __init__(self, file_path: Path):
        """
        Initialize parser.
        
        Args:
            file_path: Path to file to parse
        """
        self.file_path = file_path
        self.content = ""
        self.lines = []
        self.line_count = 0
        
    def load_file(self) -> bool:
        """
        Load file content.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8', errors='ignore') as f:
                self.content = f.read()
                self.lines = self.content.splitlines()
                self.line_count = len(self.lines)
            return True
        except (OSError, IOError) as e:
            print(f"Error loading file {self.file_path}: {e}")
            return False
    
    @abstractmethod
    def parse(self) -> Dict[str, Any]:
        """
        Parse the file and extract metadata.
        
        Returns:
            Dictionary containing parsed metadata with structure:
            {
                'classes': [...],
                'functions': [...],
                'imports': [...],
                'documentation_coverage': float
            }
        """
        pass
    
    def get_file_metadata(self) -> Dict[str, Any]:
        """
        Get basic file metadata.
        
        Returns:
            Dictionary with file metadata
        """
        return {
            'path': str(self.file_path),
            'size_bytes': self.file_path.stat().st_size if self.file_path.exists() else 0,
            'line_count': self.line_count,
        }
    
    @staticmethod
    def calculate_coverage(documented_items: int, total_items: int) -> float:
        """
        Calculate documentation coverage percentage.
        
        Args:
            documented_items: Number of documented items
            total_items: Total number of items
            
        Returns:
            Coverage percentage (0-100)
        """
        if total_items == 0:
            return 100.0
        return (documented_items / total_items) * 100.0
    
    @staticmethod
    def extract_docstring(lines: List[str], start_line: int) -> Optional[str]:
        """
        Extract docstring from lines starting at given position.
        
        Args:
            lines: List of code lines
            start_line: Starting line number (0-based)
            
        Returns:
            Docstring text or None
        """
        if start_line >= len(lines):
            return None
        
        line = lines[start_line].strip()
        
        # Check for various docstring formats
        if line.startswith('"""') or line.startswith("'''"):
            delimiter = line[:3]
            docstring_lines = []
            
            # Single-line docstring
            if line.endswith(delimiter) and len(line) > 6:
                return line[3:-3].strip()
            
            # Multi-line docstring
            docstring_lines.append(line[3:])
            for i in range(start_line + 1, len(lines)):
                line = lines[i].rstrip()
                if delimiter in line:
                    docstring_lines.append(line[:line.index(delimiter)])
                    break
                docstring_lines.append(line)
            
            return '\n'.join(docstring_lines).strip()
        
        return None
    
    @staticmethod
    def clean_comment(comment: str) -> str:
        """
        Clean comment text by removing comment markers.
        
        Args:
            comment: Raw comment text
            
        Returns:
            Cleaned comment text
        """
        # Remove common comment markers
        comment = comment.strip()
        prefixes = ['///', '//', '/*', '*/', '*', '#']
        
        for prefix in prefixes:
            if comment.startswith(prefix):
                comment = comment[len(prefix):].strip()
        
        return comment

# Made with Bob
