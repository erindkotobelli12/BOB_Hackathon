"""File filtering utilities for the codebase scanner."""

import fnmatch
from pathlib import Path
from typing import List


def should_exclude_path(path: Path, exclude_patterns: List[str]) -> bool:
    """
    Check if a path should be excluded based on patterns.
    
    Args:
        path: Path to check
        exclude_patterns: List of glob patterns to exclude
        
    Returns:
        True if path should be excluded, False otherwise
    """
    path_str = str(path).replace('\\', '/')
    
    for pattern in exclude_patterns:
        # Handle both directory and file patterns
        if fnmatch.fnmatch(path_str, pattern) or fnmatch.fnmatch(path_str, f"*/{pattern}"):
            return True
        
        # Check if any parent directory matches the pattern
        parts = path_str.split('/')
        for i in range(len(parts)):
            partial_path = '/'.join(parts[:i+1])
            if fnmatch.fnmatch(partial_path, pattern):
                return True
    
    return False


def matches_extension(path: Path, extensions: List[str]) -> bool:
    """
    Check if a file has one of the specified extensions.
    
    Args:
        path: Path to check
        extensions: List of file extensions (e.g., ['.py', '.js'])
        
    Returns:
        True if file extension matches, False otherwise
    """
    return path.suffix.lower() in [ext.lower() for ext in extensions]


def get_file_size_mb(path: Path) -> float:
    """
    Get file size in megabytes.
    
    Args:
        path: Path to file
        
    Returns:
        File size in MB
    """
    try:
        return path.stat().st_size / (1024 * 1024)
    except (OSError, IOError):
        return 0.0


def is_binary_file(path: Path, sample_size: int = 8192) -> bool:
    """
    Check if a file is binary by reading a sample.
    
    Args:
        path: Path to file
        sample_size: Number of bytes to sample
        
    Returns:
        True if file appears to be binary, False otherwise
    """
    try:
        with open(path, 'rb') as f:
            chunk = f.read(sample_size)
            
        # Check for null bytes (common in binary files)
        if b'\x00' in chunk:
            return True
            
        # Check for high ratio of non-text bytes
        text_chars = bytearray({7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7f})
        non_text = sum(1 for byte in chunk if byte not in text_chars)
        
        return non_text / len(chunk) > 0.3 if chunk else False
        
    except (OSError, IOError):
        return True

# Made with Bob
