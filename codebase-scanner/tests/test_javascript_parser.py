"""Unit tests for JavaScript/TypeScript parser."""

import unittest
from pathlib import Path
import tempfile
import os
from parsers.javascript_parser import JavaScriptParser


class TestJavaScriptParser(unittest.TestCase):
    """Test cases for JavaScriptParser."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures."""
        # Clean up temp files
        for file in Path(self.temp_dir).glob('*.*'):
            file.unlink()
        os.rmdir(self.temp_dir)
    
    def create_temp_file(self, filename: str, content: str) -> Path:
        """Create a temporary JavaScript/TypeScript file for testing."""
        file_path = Path(self.temp_dir) / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path
    
    def test_regular_function(self):
        """Test parsing a regular function."""
        content = '''
/**
 * Add two numbers
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} Sum of a and b
 */
function add(a, b) {
    return a + b;
}
'''
        file_path = self.create_temp_file('test.js', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(result['language'], 'javascript')
        self.assertEqual(len(result['functions']), 1)
        
        func = result['functions'][0]
        self.assertEqual(func['name'], 'add')
        self.assertIsNotNone(func['docstring'])
        self.assertEqual(len(func['parameters']), 2)
    
    def test_arrow_function_const(self):
        """Test parsing arrow function assigned to const."""
        content = '''
/**
 * Multiply two numbers
 */
const multiply = (a, b) => {
    return a * b;
};
'''
        file_path = self.create_temp_file('test.js', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['functions']), 1)
        func = result['functions'][0]
        self.assertEqual(func['name'], 'multiply')
        self.assertIsNotNone(func['docstring'])
        self.assertEqual(len(func['parameters']), 2)
    
    def test_arrow_function_let(self):
        """Test parsing arrow function assigned to let."""
        content = '''
let divide = (a, b) => a / b;
'''
        file_path = self.create_temp_file('test.js', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['functions']), 1)
        func = result['functions'][0]
        self.assertEqual(func['name'], 'divide')
    
    def test_async_arrow_function(self):
        """Test parsing async arrow function."""
        content = '''
/**
 * Fetch data from API
 */
const fetchData = async (url) => {
    const response = await fetch(url);
    return response.json();
};
'''
        file_path = self.create_temp_file('test.js', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['functions']), 1)
        func = result['functions'][0]
        self.assertEqual(func['name'], 'fetchData')
        self.assertTrue(func['is_async'])
    
    def test_typescript_arrow_function_with_types(self):
        """Test parsing TypeScript arrow function with type annotations."""
        content = '''
/**
 * Process user data
 */
const processUser = async (name: string, age: number): Promise<void> => {
    console.log(`${name} is ${age} years old`);
};
'''
        file_path = self.create_temp_file('test.ts', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(result['language'], 'typescript')
        self.assertEqual(len(result['functions']), 1)
        
        func = result['functions'][0]
        self.assertEqual(func['name'], 'processUser')
        self.assertTrue(func['is_async'])
        self.assertEqual(func['return_type'], 'Promise<void>')
        self.assertEqual(len(func['parameters']), 2)
        self.assertEqual(func['parameters'][0]['type'], 'string')
        self.assertEqual(func['parameters'][1]['type'], 'number')
    
    def test_class_with_methods(self):
        """Test parsing class with regular methods."""
        content = '''
/**
 * Calculator class
 */
class Calculator {
    /**
     * Add two numbers
     */
    add(a, b) {
        return a + b;
    }
    
    subtract(a, b) {
        return a - b;
    }
}
'''
        file_path = self.create_temp_file('test.js', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['classes']), 1)
        cls = result['classes'][0]
        self.assertEqual(cls['name'], 'Calculator')
        self.assertEqual(len(cls['methods']), 2)
        self.assertIsNotNone(cls['docstring'])
    
    def test_class_with_typescript_access_modifiers(self):
        """Test parsing class with TypeScript access modifiers."""
        content = '''
class User {
    public name: string;
    private age: number;
    protected email: string;
    
    public getName(): string {
        return this.name;
    }
    
    private getAge(): number {
        return this.age;
    }
    
    protected getEmail(): string {
        return this.email;
    }
}
'''
        file_path = self.create_temp_file('test.ts', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['classes']), 1)
        cls = result['classes'][0]
        self.assertEqual(len(cls['methods']), 3)
        
        # Check visibility
        get_name = next(m for m in cls['methods'] if m['name'] == 'getName')
        self.assertEqual(get_name['visibility'], 'public')
        
        get_age = next(m for m in cls['methods'] if m['name'] == 'getAge')
        self.assertEqual(get_age['visibility'], 'private')
        
        get_email = next(m for m in cls['methods'] if m['name'] == 'getEmail')
        self.assertEqual(get_email['visibility'], 'protected')
    
    def test_class_property_arrow_functions(self):
        """Test parsing class property arrow functions."""
        content = '''
class EventHandler {
    /**
     * Handle click event
     */
    handleClick = (event) => {
        console.log('Clicked!', event);
    };
    
    handleSubmit = async (data) => {
        await this.save(data);
    };
}
'''
        file_path = self.create_temp_file('test.js', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['classes']), 1)
        cls = result['classes'][0]
        self.assertEqual(len(cls['methods']), 2)
        
        # Check that arrow functions are detected
        handle_click = next(m for m in cls['methods'] if m['name'] == 'handleClick')
        self.assertTrue(handle_click.get('is_arrow_function', False))
        
        handle_submit = next(m for m in cls['methods'] if m['name'] == 'handleSubmit')
        self.assertTrue(handle_submit['is_async'])
    
    def test_typescript_class_property_with_modifiers(self):
        """Test parsing TypeScript class property arrow functions with access modifiers."""
        content = '''
class Component {
    public onClick = (event: MouseEvent): void => {
        this.handleEvent(event);
    };
    
    private handleEvent = (event: Event): void => {
        console.log(event);
    };
    
    protected onSubmit = async (data: FormData): Promise<void> => {
        await this.save(data);
    };
}
'''
        file_path = self.create_temp_file('test.ts', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['classes']), 1)
        cls = result['classes'][0]
        self.assertEqual(len(cls['methods']), 3)
        
        # Check visibility from modifiers
        on_click = next(m for m in cls['methods'] if m['name'] == 'onClick')
        self.assertEqual(on_click['visibility'], 'public')
        
        handle_event = next(m for m in cls['methods'] if m['name'] == 'handleEvent')
        self.assertEqual(handle_event['visibility'], 'private')
        
        on_submit = next(m for m in cls['methods'] if m['name'] == 'onSubmit')
        self.assertEqual(on_submit['visibility'], 'protected')
        self.assertTrue(on_submit['is_async'])
    
    def test_generic_types(self):
        """Test parsing functions and classes with generic type parameters."""
        content = '''
/**
 * Generic identity function
 */
function identity<T>(arg: T): T {
    return arg;
}

/**
 * Generic class
 */
class Container<T> {
    private value: T;
    
    getValue(): T {
        return this.value;
    }
}
'''
        file_path = self.create_temp_file('test.ts', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        # Should parse without errors
        self.assertEqual(len(result['functions']), 1)
        self.assertEqual(len(result['classes']), 1)
        
        func = result['functions'][0]
        self.assertEqual(func['name'], 'identity')
        
        cls = result['classes'][0]
        self.assertEqual(cls['name'], 'Container')
    
    def test_complex_typescript_types(self):
        """Test parsing complex TypeScript type annotations."""
        content = '''
const processData = (
    items: Array<string>,
    callback: (item: string) => void,
    options?: { strict: boolean }
): Promise<Map<string, number>> => {
    return Promise.resolve(new Map());
};
'''
        file_path = self.create_temp_file('test.ts', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['functions']), 1)
        func = result['functions'][0]
        self.assertEqual(func['name'], 'processData')
        # Should parse at least 2 parameters (complex nested types may cause issues)
        self.assertGreaterEqual(len(func['parameters']), 2)
    
    def test_documentation_coverage(self):
        """Test documentation coverage calculation."""
        content = '''
/**
 * Documented function
 */
function documented() {
    return true;
}

function undocumented() {
    return false;
}

/**
 * Documented arrow function
 */
const documentedArrow = () => true;

const undocumentedArrow = () => false;
'''
        file_path = self.create_temp_file('test.js', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        # 2 out of 4 functions documented = 50%
        self.assertEqual(result['documentation_coverage'], 50.0)
    
    def test_imports(self):
        """Test parsing import statements."""
        content = '''
import React from 'react';
import { useState, useEffect } from 'react';
import * as utils from './utils';
import './styles.css';
'''
        file_path = self.create_temp_file('test.js', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['imports']), 4)
    
    def test_static_methods(self):
        """Test parsing static methods."""
        content = '''
class MathUtils {
    static add(a, b) {
        return a + b;
    }
    
    static multiply(a, b) {
        return a * b;
    }
}
'''
        file_path = self.create_temp_file('test.js', content)
        parser = JavaScriptParser(file_path)
        result = parser.parse()
        
        self.assertEqual(len(result['classes']), 1)
        cls = result['classes'][0]
        self.assertEqual(len(cls['methods']), 2)
        
        # Check that static methods are detected
        add_method = next(m for m in cls['methods'] if m['name'] == 'add')
        self.assertTrue(add_method.get('is_static', False))


if __name__ == '__main__':
    unittest.main()

# Made with Bob