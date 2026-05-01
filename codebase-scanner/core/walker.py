"""Directory traversal for scanning codebases."""

import logging
from pathlib import Path
from typing import List, Iterator
from ..utils.filters import should_exclude_path, matches_extension, get_file_size_mb, is_binary_file


class DirectoryWalker:
    """Walks through directory structure and yields files for scanning."""
    
    def __init__(
        self,
        root_dir: Path,
        exclude_patterns: List[str],
        include_extensions: List[str],
        max_file_size_mb: float = 10.0,
        follow_symlinks: bool = False,
        logger: logging.Logger | None = None
    ):
        """
        Initialize directory walker.
        
        Args:
            root_dir: Root directory to scan
            exclude_patterns: List of glob patterns to exclude
            include_extensions: List of file extensions to include
            max_file_size_mb: Maximum file size in MB
            follow_symlinks: Whether to follow symbolic links
            logger: Logger instance
        """
        self.root_dir = Path(root_dir).resolve()
        self.exclude_patterns = exclude_patterns
        self.include_extensions = include_extensions
        self.max_file_size_mb = max_file_size_mb
        self.follow_symlinks = follow_symlinks
        self.logger = logger or logging.getLogger(__name__)
        
        self.stats = {
            'total_files': 0,
            'skipped_excluded': 0,
            'skipped_extension': 0,
            'skipped_size': 0,
            'skipped_binary': 0,
            'skipped_error': 0,
        }
    
    def walk(self) -> Iterator[Path]:
        """
        Walk through directory and yield files to scan.
        
        Yields:
            Path objects for files that pass all filters
        """
        self.logger.info(f"Starting directory walk from: {self.root_dir}")
        
        if not self.root_dir.exists():
            self.logger.error(f"Root directory does not exist: {self.root_dir}")
            return
        
        if not self.root_dir.is_dir():
            self.logger.error(f"Root path is not a directory: {self.root_dir}")
            return
        
        try:
            for file_path in self._walk_recursive(self.root_dir):
                yield file_path
        except Exception as e:
            self.logger.error(f"Error during directory walk: {e}")
        
        self._log_stats()
    
    def _walk_recursive(self, directory: Path) -> Iterator[Path]:
        """
        Recursively walk through directory.
        
        Args:
            directory: Directory to walk
            
        Yields:
            Path objects for valid files
        """
        try:
            entries = sorted(directory.iterdir())
        except (PermissionError, OSError) as e:
            self.logger.warning(f"Cannot access directory {directory}: {e}")
            return
        
        for entry in entries:
            # Skip symlinks if not following them
            if entry.is_symlink() and not self.follow_symlinks:
                continue
            
            # Check exclusion patterns
            if should_exclude_path(entry, self.exclude_patterns):
                self.stats['skipped_excluded'] += 1
                continue
            
            if entry.is_dir():
                # Recursively walk subdirectories
                yield from self._walk_recursive(entry)
            elif entry.is_file():
                # Process file
                if self._should_process_file(entry):
                    self.stats['total_files'] += 1
                    yield entry
    
    def _should_process_file(self, file_path: Path) -> bool:
        """
        Check if a file should be processed.
        
        Args:
            file_path: Path to file
            
        Returns:
            True if file should be processed
        """
        # Check extension
        if not matches_extension(file_path, self.include_extensions):
            self.stats['skipped_extension'] += 1
            return False
        
        # Check file size
        try:
            file_size = get_file_size_mb(file_path)
            if file_size > self.max_file_size_mb:
                self.logger.warning(
                    f"Skipping large file ({file_size:.2f}MB): {file_path}"
                )
                self.stats['skipped_size'] += 1
                return False
        except Exception as e:
            self.logger.warning(f"Error checking file size for {file_path}: {e}")
            self.stats['skipped_error'] += 1
            return False
        
        # Check if binary
        try:
            if is_binary_file(file_path):
                self.logger.debug(f"Skipping binary file: {file_path}")
                self.stats['skipped_binary'] += 1
                return False
        except Exception as e:
            self.logger.warning(f"Error checking if binary {file_path}: {e}")
            self.stats['skipped_error'] += 1
            return False
        
        return True
    
    def _log_stats(self) -> None:
        """Log statistics about the walk."""
        self.logger.info("Directory walk completed")
        self.logger.info(f"Files to process: {self.stats['total_files']}")
        self.logger.info(f"Skipped (excluded): {self.stats['skipped_excluded']}")
        self.logger.info(f"Skipped (extension): {self.stats['skipped_extension']}")
        self.logger.info(f"Skipped (size): {self.stats['skipped_size']}")
        self.logger.info(f"Skipped (binary): {self.stats['skipped_binary']}")
        self.logger.info(f"Skipped (error): {self.stats['skipped_error']}")
    
    def get_stats(self) -> dict:
        """
        Get walk statistics.
        
        Returns:
            Dictionary of statistics
        """
        return self.stats.copy()

# Made with Bob
