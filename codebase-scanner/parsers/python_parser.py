"""Python-specific parser using AST."""

import ast
from pathlib import Path
from typing import Dict, List, Any, Optional
from .base_parser import BaseParser


class PythonParser(BaseParser):
    """Parser for Python source files using AST."""
    
    def __init__(self, file_path: Path):
        """
        Initialize Python parser.
        
        Args:
            file_path: Path to Python file
        """
        super().__init__(file_path)
        self.tree = None
    
    def parse(self) -> Dict[str, Any]:
        """
        Parse Python file and extract metadata.
        
        Returns:
            Dictionary containing classes, functions, imports, and coverage
        """
        if not self.load_file():
            return self._empty_result()
        
        try:
            self.tree = ast.parse(self.content, filename=str(self.file_path))
        except SyntaxError as e:
            print(f"Syntax error in {self.file_path}: {e}")
            return self._empty_result()
        
        classes = self._extract_classes()
        functions = self._extract_functions()
        imports = self._extract_imports()
        
        # Calculate documentation coverage
        total_items = len(functions) + sum(len(cls['methods']) for cls in classes)
        documented_items = sum(
            1 for f in functions if f.get('docstring')
        ) + sum(
            1 for cls in classes for m in cls['methods'] if m.get('docstring')
        )
        
        coverage = self.calculate_coverage(documented_items, total_items)
        
        result = self.get_file_metadata()
        result.update({
            'language': 'python',
            'classes': classes,
            'functions': functions,
            'imports': imports,
            'documentation_coverage': coverage,
        })
        
        return result
    
    def _extract_classes(self) -> List[Dict[str, Any]]:
        """Extract class definitions from AST."""
        classes = []
        
        if self.tree is None:
            return classes
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                class_info = {
                    'name': node.name,
                    'line_start': node.lineno,
                    'line_end': node.end_lineno or node.lineno,
                    'docstring': ast.get_docstring(node),
                    'methods': self._extract_methods(node),
                    'base_classes': [self._get_name(base) for base in node.bases],
                    'decorators': [self._get_decorator_name(dec) for dec in node.decorator_list],
                }
                classes.append(class_info)
        
        return classes
    
    def _extract_methods(self, class_node: ast.ClassDef) -> List[Dict[str, Any]]:
        """Extract method definitions from a class."""
        methods = []
        
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                method_info = self._extract_function_info(node)
                method_info['visibility'] = self._get_visibility(node.name)
                methods.append(method_info)
        
        return methods
    
    def _extract_functions(self) -> List[Dict[str, Any]]:
        """Extract top-level function definitions."""
        functions = []
        
        if self.tree is None:
            return functions
        
        for node in self.tree.body:
            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                functions.append(self._extract_function_info(node))
        
        return functions
    
    def _extract_function_info(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> Dict[str, Any]:
        """Extract information from a function node."""
        return {
            'name': node.name,
            'line_start': node.lineno,
            'line_end': node.end_lineno or node.lineno,
            'parameters': self._extract_parameters(node),
            'return_type': self._get_return_annotation(node),
            'docstring': ast.get_docstring(node),
            'decorators': [self._get_decorator_name(dec) for dec in node.decorator_list],
            'is_async': isinstance(node, ast.AsyncFunctionDef),
        }
    
    def _extract_parameters(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> List[Dict[str, Any]]:
        """Extract function parameters with type hints and defaults."""
        params = []
        args = node.args
        
        # Regular arguments
        defaults_offset = len(args.args) - len(args.defaults)
        for i, arg in enumerate(args.args):
            default_value = None
            if i >= defaults_offset:
                default_idx = i - defaults_offset
                default_value = self._get_default_value(args.defaults[default_idx])
            
            params.append({
                'name': arg.arg,
                'type': self._get_annotation(arg.annotation),
                'default': default_value,
            })
        
        # *args
        if args.vararg:
            params.append({
                'name': f"*{args.vararg.arg}",
                'type': self._get_annotation(args.vararg.annotation),
                'default': None,
            })
        
        # **kwargs
        if args.kwarg:
            params.append({
                'name': f"**{args.kwarg.arg}",
                'type': self._get_annotation(args.kwarg.annotation),
                'default': None,
            })
        
        return params
    
    def _extract_imports(self) -> List[str]:
        """Extract import statements."""
        imports = []
        
        if self.tree is None:
            return imports
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(f"import {alias.name}")
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ''
                for alias in node.names:
                    imports.append(f"from {module} import {alias.name}")
        
        return imports
    
    def _get_annotation(self, annotation) -> Optional[str]:
        """Get string representation of type annotation."""
        if annotation is None:
            return None
        return ast.unparse(annotation)
    
    def _get_return_annotation(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> Optional[str]:
        """Get return type annotation."""
        if node.returns:
            return ast.unparse(node.returns)
        return None
    
    def _get_default_value(self, node) -> Optional[str]:
        """Get string representation of default value."""
        try:
            return ast.unparse(node)
        except:
            return None
    
    def _get_decorator_name(self, decorator) -> str:
        """Get decorator name."""
        if isinstance(decorator, ast.Name):
            return f"@{decorator.id}"
        elif isinstance(decorator, ast.Call):
            return f"@{ast.unparse(decorator.func)}"
        return f"@{ast.unparse(decorator)}"
    
    def _get_name(self, node) -> str:
        """Get name from AST node."""
        if isinstance(node, ast.Name):
            return node.id
        return ast.unparse(node)
    
    def _get_visibility(self, name: str) -> str:
        """Determine visibility from name."""
        if name.startswith('__') and not name.endswith('__'):
            return 'private'
        elif name.startswith('_'):
            return 'protected'
        return 'public'
    
    def _empty_result(self) -> Dict[str, Any]:
        """Return empty result structure."""
        result = self.get_file_metadata()
        result.update({
            'language': 'python',
            'classes': [],
            'functions': [],
            'imports': [],
            'documentation_coverage': 0.0,
        })
        return result

# Made with Bob
