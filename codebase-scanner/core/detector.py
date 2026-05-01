"""Language detection for source code files."""

from pathlib import Path
from typing import Optional


class LanguageDetector:
    """Detects programming language from file extensions and content."""
    
    # Map file extensions to language names
    EXTENSION_MAP = {
        '.py': 'python',
        '.js': 'javascript',
        '.jsx': 'javascript',
        '.ts': 'typescript',
        '.tsx': 'typescript',
        '.java': 'java',
        '.c': 'c',
        '.h': 'c',
        '.cpp': 'cpp',
        '.cc': 'cpp',
        '.cxx': 'cpp',
        '.hpp': 'cpp',
        '.hh': 'cpp',
        '.hxx': 'cpp',
        '.go': 'go',
        '.rs': 'rust',
        '.rb': 'ruby',
        '.php': 'php',
        '.cs': 'csharp',
        '.swift': 'swift',
        '.kt': 'kotlin',
        '.scala': 'scala',
        '.m': 'objective-c',
        '.mm': 'objective-cpp',
    }
    
    # Shebang patterns for script detection
    SHEBANG_MAP = {
        'python': ['python', 'python3', 'python2'],
        'ruby': ['ruby'],
        'bash': ['bash', 'sh'],
        'perl': ['perl'],
        'node': ['node'],
    }
    
    @classmethod
    def detect_language(cls, file_path: Path) -> Optional[str]:
        """
        Detect the programming language of a file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Language name or None if not detected
        """
        # First try extension-based detection
        extension = file_path.suffix.lower()
        if extension in cls.EXTENSION_MAP:
            return cls.EXTENSION_MAP[extension]
        
        # Try shebang detection for files without extension
        if not extension or extension == '.sh':
            language = cls._detect_from_shebang(file_path)
            if language:
                return language
        
        return None
    
    @classmethod
    def _detect_from_shebang(cls, file_path: Path) -> Optional[str]:
        """
        Detect language from shebang line.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Language name or None
        """
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                first_line = f.readline().strip()
                
            if first_line.startswith('#!'):
                shebang = first_line[2:].lower()
                
                for language, interpreters in cls.SHEBANG_MAP.items():
                    if any(interp in shebang for interp in interpreters):
                        return language
                        
        except (OSError, IOError, UnicodeDecodeError):
            pass
            
        return None
    
    @classmethod
    def get_supported_languages(cls) -> list[str]:
        """
        Get list of supported languages.
        
        Returns:
            List of language names
        """
        return sorted(set(cls.EXTENSION_MAP.values()))
    
    @classmethod
    def get_extensions_for_language(cls, language: str) -> list[str]:
        """
        Get file extensions for a specific language.
        
        Args:
            language: Language name
            
        Returns:
            List of file extensions
        """
        return [ext for ext, lang in cls.EXTENSION_MAP.items() if lang == language]

# Made with Bob
