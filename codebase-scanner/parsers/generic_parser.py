"""Generic fallback parser for unsupported languages."""

from pathlib import Path
from typing import Dict, Any
from .base_parser import BaseParser


class GenericParser(BaseParser):
    """Fallback parser for languages without specific support."""
    
    def __init__(self, file_path: Path):
        """
        Initialize generic parser.
        
        Args:
            file_path: Path to file
        """
        super().__init__(file_path)
    
    def parse(self) -> Dict[str, Any]:
        """
        Parse file with basic metadata only.
        
        Returns:
            Dictionary with minimal metadata
        """
        if not self.load_file():
            return self._empty_result()
        
        result = self.get_file_metadata()
        result.update({
            'language': 'unknown',
            'classes': [],
            'functions': [],
            'imports': [],
            'documentation_coverage': 0.0,
            'note': 'Language-specific parsing not supported. Only basic file metadata available.',
        })
        
        return result
    
    def _empty_result(self) -> Dict[str, Any]:
        """Return empty result structure."""
        result = self.get_file_metadata()
        result.update({
            'language': 'unknown',
            'classes': [],
            'functions': [],
            'imports': [],
            'documentation_coverage': 0.0,
        })
        return result

# Made with Bob
