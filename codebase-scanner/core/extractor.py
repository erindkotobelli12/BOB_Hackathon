"""Metadata extraction engine that coordinates parsers."""

import logging
from pathlib import Path
from typing import Dict, Any, Optional
from core.detector import LanguageDetector
from parsers import (
    PythonParser,
    JavaScriptParser,
    JavaParser,
    CppParser,
    GenericParser,
)


class MetadataExtractor:
    """Extracts metadata from source files using appropriate parsers."""
    
    # Map languages to parser classes
    PARSER_MAP = {
        'python': PythonParser,
        'javascript': JavaScriptParser,
        'typescript': JavaScriptParser,
        'java': JavaParser,
        'c': CppParser,
        'cpp': CppParser,
    }
    
    def __init__(self, logger: logging.Logger | None = None):
        """
        Initialize metadata extractor.
        
        Args:
            logger: Logger instance
        """
        self.logger = logger or logging.getLogger(__name__)
        self.detector = LanguageDetector()
    
    def extract(self, file_path: Path) -> Dict[str, Any]:
        """
        Extract metadata from a file.
        
        Args:
            file_path: Path to file
            
        Returns:
            Dictionary containing extracted metadata
        """
        try:
            # Detect language
            language = self.detector.detect_language(file_path)
            
            if language is None:
                self.logger.warning(f"Could not detect language for: {file_path}")
                return self._use_generic_parser(file_path)
            
            # Get appropriate parser
            parser_class = self.PARSER_MAP.get(language, GenericParser)
            
            self.logger.debug(f"Parsing {file_path} as {language}")
            
            # Parse file
            parser = parser_class(file_path)
            metadata = parser.parse()
            
            return metadata
            
        except Exception as e:
            self.logger.error(f"Error extracting metadata from {file_path}: {e}")
            return self._error_result(file_path, str(e))
    
    def _use_generic_parser(self, file_path: Path) -> Dict[str, Any]:
        """Use generic parser as fallback."""
        self.logger.debug(f"Using generic parser for: {file_path}")
        parser = GenericParser(file_path)
        return parser.parse()
    
    def _error_result(self, file_path: Path, error: str) -> Dict[str, Any]:
        """Return error result structure."""
        return {
            'path': str(file_path),
            'language': 'unknown',
            'size_bytes': 0,
            'line_count': 0,
            'classes': [],
            'functions': [],
            'imports': [],
            'documentation_coverage': 0.0,
            'error': error,
        }
    
    def get_supported_languages(self) -> list[str]:
        """
        Get list of languages with dedicated parsers.
        
        Returns:
            List of supported language names
        """
        return list(self.PARSER_MAP.keys())

# Made with Bob
