"""Unit tests for file filters."""

import unittest
from pathlib import Path
import tempfile
import os
from utils.filters import should_exclude_path, matches_extension, get_file_size_mb, is_binary_file


class TestFilters(unittest.TestCase):
    """Test cases for file filtering utilities."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures."""
        for file in Path(self.temp_dir).glob('*'):
            file.unlink()
        os.rmdir(self.temp_dir)
    
    def test_should_exclude_path_simple(self):
        """Test simple exclusion pattern."""
        path = Path('node_modules/package/file.js')
        patterns = ['node_modules/**']
        self.assertTrue(should_exclude_path(path, patterns))
    
    def test_should_exclude_path_no_match(self):
        """Test path that should not be excluded."""
        path = Path('src/main.py')
        patterns = ['node_modules/**', 'venv/**']
        self.assertFalse(should_exclude_path(path, patterns))
    
    def test_should_exclude_path_wildcard(self):
        """Test wildcard exclusion pattern."""
        path = Path('dist/bundle.min.js')
        patterns = ['*.min.js']
        self.assertTrue(should_exclude_path(path, patterns))
    
    def test_matches_extension_positive(self):
        """Test matching file extension."""
        path = Path('test.py')
        extensions = ['.py', '.js', '.java']
        self.assertTrue(matches_extension(path, extensions))
    
    def test_matches_extension_negative(self):
        """Test non-matching file extension."""
        path = Path('test.txt')
        extensions = ['.py', '.js', '.java']
        self.assertFalse(matches_extension(path, extensions))
    
    def test_matches_extension_case_insensitive(self):
        """Test case-insensitive extension matching."""
        path = Path('Test.PY')
        extensions = ['.py']
        self.assertTrue(matches_extension(path, extensions))
    
    def test_get_file_size_mb(self):
        """Test file size calculation."""
        # Create a test file
        file_path = Path(self.temp_dir) / 'test.txt'
        with open(file_path, 'w') as f:
            f.write('x' * 1024 * 1024)  # 1MB
        
        size = get_file_size_mb(file_path)
        self.assertAlmostEqual(size, 1.0, places=1)
    
    def test_is_binary_file_text(self):
        """Test text file detection."""
        file_path = Path(self.temp_dir) / 'test.txt'
        with open(file_path, 'w') as f:
            f.write('This is a text file')
        
        self.assertFalse(is_binary_file(file_path))
    
    def test_is_binary_file_binary(self):
        """Test binary file detection."""
        file_path = Path(self.temp_dir) / 'test.bin'
        with open(file_path, 'wb') as f:
            f.write(b'\x00\x01\x02\x03\x04\x05')
        
        self.assertTrue(is_binary_file(file_path))


if __name__ == '__main__':
    unittest.main()

# Made with Bob
