"""Unit tests for language detector."""

import unittest
from pathlib import Path
import tempfile
import os
from core.detector import LanguageDetector


class TestLanguageDetector(unittest.TestCase):
    """Test cases for LanguageDetector."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.detector = LanguageDetector()
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures."""
        for file in Path(self.temp_dir).glob('*'):
            file.unlink()
        os.rmdir(self.temp_dir)
    
    def create_temp_file(self, filename: str, content: str = '') -> Path:
        """Create a temporary file for testing."""
        file_path = Path(self.temp_dir) / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path
    
    def test_python_detection(self):
        """Test Python file detection."""
        file_path = self.create_temp_file('test.py')
        language = self.detector.detect_language(file_path)
        self.assertEqual(language, 'python')
    
    def test_javascript_detection(self):
        """Test JavaScript file detection."""
        file_path = self.create_temp_file('test.js')
        language = self.detector.detect_language(file_path)
        self.assertEqual(language, 'javascript')
    
    def test_typescript_detection(self):
        """Test TypeScript file detection."""
        file_path = self.create_temp_file('test.ts')
        language = self.detector.detect_language(file_path)
        self.assertEqual(language, 'typescript')
    
    def test_java_detection(self):
        """Test Java file detection."""
        file_path = self.create_temp_file('Test.java')
        language = self.detector.detect_language(file_path)
        self.assertEqual(language, 'java')
    
    def test_c_detection(self):
        """Test C file detection."""
        file_path = self.create_temp_file('test.c')
        language = self.detector.detect_language(file_path)
        self.assertEqual(language, 'c')
    
    def test_cpp_detection(self):
        """Test C++ file detection."""
        file_path = self.create_temp_file('test.cpp')
        language = self.detector.detect_language(file_path)
        self.assertEqual(language, 'cpp')
    
    def test_shebang_python(self):
        """Test Python detection via shebang."""
        content = '#!/usr/bin/env python3\nprint("Hello")'
        file_path = self.create_temp_file('script', content)
        language = self.detector.detect_language(file_path)
        self.assertEqual(language, 'python')
    
    def test_unknown_extension(self):
        """Test unknown file extension."""
        file_path = self.create_temp_file('test.xyz')
        language = self.detector.detect_language(file_path)
        self.assertIsNone(language)
    
    def test_get_supported_languages(self):
        """Test getting list of supported languages."""
        languages = self.detector.get_supported_languages()
        self.assertIn('python', languages)
        self.assertIn('javascript', languages)
        self.assertIn('java', languages)
    
    def test_get_extensions_for_language(self):
        """Test getting extensions for a language."""
        extensions = self.detector.get_extensions_for_language('python')
        self.assertIn('.py', extensions)
        
        extensions = self.detector.get_extensions_for_language('cpp')
        self.assertIn('.cpp', extensions)
        self.assertIn('.hpp', extensions)


if __name__ == '__main__':
    unittest.main()

# Made with Bob
