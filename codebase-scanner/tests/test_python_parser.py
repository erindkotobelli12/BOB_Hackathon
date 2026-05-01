"""Unit tests for Python parser."""

import unittest
from pathlib import Path
import tempfile
import os
from parsers.python_parser import PythonParser


class TestPythonParser(unittest.TestCase):
    """Test cases for PythonParser."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures."""
        # Clean up temp files
        for file in Path(self.temp_dir).glob('*.py'):
            file.unlink()
        os.rmdir(self.temp_dir)
    
    def create_temp_file(self, filename: str, content: str) -> Path:
        """Create a temporary Python file for testing."""
        file_path = Path(self.temp_dir) / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path
    
    def test_simple_function(self):
        """Test parsing a simple function."""
        content = '''
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
'''
        file_path = self.create_temp_file('test.py', content)
        parser = PythonParser(file_path)
        result = parser.parse()
        
        self.assertEqual(result['language'], 'python')
        self.assertEqual(len(result['functions']), 1)
        
        func = result['functions'][0]
        self.assertEqual(func['name'], 'add')
        self.assertEqual(func['return_type'], 'int')
        self.assertEqual(func['docstring'], 'Add two numbers.')
        self.assertEqual(len(func['parameters']), 2)
    
    def test_class_with_methods(self):
        """Test parsing a class with methods."""
        content = '''
class Calculator:
    """A simple calculator class."""
    
    def add(self, a: int, b: int) -> int:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        """Subtract b from a."""
        return a - b
'''
        file_path = self.create_temp_file('test.py', content)
        parser = PythonParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['classes']), 1)
        
        cls = result['classes'][0]
        self.assertEqual(cls['name'], 'Calculator')
        self.assertEqual(cls['docstring'], 'A simple calculator class.')
        self.assertEqual(len(cls['methods']), 2)
    
    def test_async_function(self):
        """Test parsing async function."""
        content = '''
async def fetch_data(url: str) -> dict:
    """Fetch data from URL."""
    pass
'''
        file_path = self.create_temp_file('test.py', content)
        parser = PythonParser(file_path)
        result = parser.parse()
        
        func = result['functions'][0]
        self.assertTrue(func['is_async'])
    
    def test_decorated_function(self):
        """Test parsing decorated function."""
        content = '''
@staticmethod
def helper():
    """Helper function."""
    pass
'''
        file_path = self.create_temp_file('test.py', content)
        parser = PythonParser(file_path)
        result = parser.parse()
        
        func = result['functions'][0]
        self.assertIn('@staticmethod', func['decorators'])
    
    def test_imports(self):
        """Test parsing import statements."""
        content = '''
import os
from typing import List, Dict
from pathlib import Path
'''
        file_path = self.create_temp_file('test.py', content)
        parser = PythonParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['imports']), 3)
        self.assertIn('import os', result['imports'])
    
    def test_documentation_coverage(self):
        """Test documentation coverage calculation."""
        content = '''
def documented():
    """This is documented."""
    pass

def undocumented():
    pass
'''
        file_path = self.create_temp_file('test.py', content)
        parser = PythonParser(file_path)
        result = parser.parse()
        
        # 1 out of 2 functions documented = 50%
        self.assertEqual(result['documentation_coverage'], 50.0)
    
    def test_syntax_error(self):
        """Test handling of syntax errors."""
        content = '''
def broken(
    # Missing closing parenthesis
'''
        file_path = self.create_temp_file('test.py', content)
        parser = PythonParser(file_path)
        result = parser.parse()
        
        # Should return empty result on syntax error
        self.assertEqual(len(result['functions']), 0)
        self.assertEqual(len(result['classes']), 0)


if __name__ == '__main__':
    unittest.main()

# Made with Bob
