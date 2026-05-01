"""JavaScript/TypeScript parser using regex patterns."""

import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from .base_parser import BaseParser


class JavaScriptParser(BaseParser):
    """Parser for JavaScript and TypeScript files."""
    
    # Regex patterns for parsing
    CLASS_PATTERN = re.compile(
        r'(?:export\s+)?(?:default\s+)?class\s+(\w+)(?:\s+extends\s+([\w.]+))?',
        re.MULTILINE
    )
    FUNCTION_PATTERN = re.compile(
        r'(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\((.*?)\)(?:\s*:\s*([\w<>[\]|]+))?',
        re.MULTILINE | re.DOTALL
    )
    ARROW_FUNCTION_PATTERN = re.compile(
        r'(?:export\s+)?(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\((.*?)\)(?:\s*:\s*([\w<>[\]|]+))?\s*=>',
        re.MULTILINE | re.DOTALL
    )
    METHOD_PATTERN = re.compile(
        r'(?:async\s+)?(\w+)\s*\((.*?)\)(?:\s*:\s*([\w<>[\]|]+))?\s*\{',
        re.MULTILINE | re.DOTALL
    )
    JSDOC_PATTERN = re.compile(
        r'/\*\*(.*?)\*/',
        re.DOTALL
    )
    IMPORT_PATTERN = re.compile(
        r'import\s+.*?from\s+[\'"].*?[\'"]|import\s+[\'"].*?[\'"]',
        re.MULTILINE
    )
    
    def __init__(self, file_path: Path):
        """
        Initialize JavaScript/TypeScript parser.
        
        Args:
            file_path: Path to JS/TS file
        """
        super().__init__(file_path)
        self.is_typescript = file_path.suffix in ['.ts', '.tsx']
    
    def parse(self) -> Dict[str, Any]:
        """
        Parse JavaScript/TypeScript file and extract metadata.
        
        Returns:
            Dictionary containing classes, functions, imports, and coverage
        """
        if not self.load_file():
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
            'language': 'typescript' if self.is_typescript else 'javascript',
            'classes': classes,
            'functions': functions,
            'imports': imports,
            'documentation_coverage': coverage,
        })
        
        return result
    
    def _extract_classes(self) -> List[Dict[str, Any]]:
        """Extract class definitions."""
        classes = []
        
        for match in self.CLASS_PATTERN.finditer(self.content):
            class_name = match.group(1)
            base_class = match.group(2) if match.group(2) else None
            line_start = self.content[:match.start()].count('\n') + 1
            
            # Find class body
            class_start = match.end()
            brace_count = 0
            class_end = class_start
            
            for i, char in enumerate(self.content[class_start:], class_start):
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        class_end = i
                        break
            
            line_end = self.content[:class_end].count('\n') + 1
            class_body = self.content[class_start:class_end]
            
            # Extract JSDoc before class
            docstring = self._extract_jsdoc_before(match.start())
            
            # Extract methods
            methods = self._extract_methods(class_body, line_start)
            
            classes.append({
                'name': class_name,
                'line_start': line_start,
                'line_end': line_end,
                'docstring': docstring,
                'methods': methods,
                'base_classes': [base_class] if base_class else [],
                'decorators': [],
            })
        
        return classes
    
    def _extract_methods(self, class_body: str, class_line_start: int) -> List[Dict[str, Any]]:
        """Extract method definitions from class body."""
        methods = []
        
        for match in self.METHOD_PATTERN.finditer(class_body):
            method_name = match.group(1)
            
            # Skip constructor and common non-methods
            if method_name in ['if', 'for', 'while', 'switch', 'catch']:
                continue
            
            params_str = match.group(2)
            return_type = match.group(3)
            
            line_offset = class_body[:match.start()].count('\n')
            line_start = class_line_start + line_offset
            
            # Extract JSDoc
            docstring = self._extract_jsdoc_before_in_text(class_body, match.start())
            
            methods.append({
                'name': method_name,
                'line_start': line_start,
                'line_end': line_start + 1,  # Approximate
                'parameters': self._parse_parameters(params_str),
                'return_type': return_type,
                'docstring': docstring,
                'decorators': [],
                'is_async': 'async' in class_body[max(0, match.start()-10):match.start()],
                'visibility': self._get_visibility(method_name),
            })
        
        return methods
    
    def _extract_functions(self) -> List[Dict[str, Any]]:
        """Extract top-level function definitions."""
        functions = []
        
        # Regular functions
        for match in self.FUNCTION_PATTERN.finditer(self.content):
            func_name = match.group(1)
            params_str = match.group(2)
            return_type = match.group(3)
            line_start = self.content[:match.start()].count('\n') + 1
            
            docstring = self._extract_jsdoc_before(match.start())
            
            functions.append({
                'name': func_name,
                'line_start': line_start,
                'line_end': line_start + 1,  # Approximate
                'parameters': self._parse_parameters(params_str),
                'return_type': return_type,
                'docstring': docstring,
                'decorators': [],
                'is_async': 'async' in self.content[max(0, match.start()-10):match.start()],
            })
        
        # Arrow functions
        for match in self.ARROW_FUNCTION_PATTERN.finditer(self.content):
            func_name = match.group(1)
            params_str = match.group(2)
            return_type = match.group(3)
            line_start = self.content[:match.start()].count('\n') + 1
            
            docstring = self._extract_jsdoc_before(match.start())
            
            functions.append({
                'name': func_name,
                'line_start': line_start,
                'line_end': line_start + 1,  # Approximate
                'parameters': self._parse_parameters(params_str),
                'return_type': return_type,
                'docstring': docstring,
                'decorators': [],
                'is_async': 'async' in self.content[max(0, match.start()-10):match.start()],
            })
        
        return functions
    
    def _parse_parameters(self, params_str: str) -> List[Dict[str, Any]]:
        """Parse function parameters."""
        if not params_str.strip():
            return []
        
        params = []
        # Simple split by comma (doesn't handle complex nested types perfectly)
        for param in params_str.split(','):
            param = param.strip()
            if not param:
                continue
            
            # Parse name, type, and default
            name = param
            param_type = None
            default = None
            
            # Check for default value
            if '=' in param:
                parts = param.split('=', 1)
                param = parts[0].strip()
                default = parts[1].strip()
            
            # Check for type annotation
            if ':' in param:
                parts = param.split(':', 1)
                name = parts[0].strip()
                param_type = parts[1].strip()
            else:
                name = param
            
            params.append({
                'name': name,
                'type': param_type,
                'default': default,
            })
        
        return params
    
    def _extract_imports(self) -> List[str]:
        """Extract import statements."""
        imports = []
        
        for match in self.IMPORT_PATTERN.finditer(self.content):
            imports.append(match.group(0).strip())
        
        return imports
    
    def _extract_jsdoc_before(self, position: int) -> Optional[str]:
        """Extract JSDoc comment before a position."""
        # Look backwards for JSDoc
        text_before = self.content[:position]
        matches = list(self.JSDOC_PATTERN.finditer(text_before))
        
        if matches:
            last_match = matches[-1]
            # Check if JSDoc is close to the position (within 2 lines)
            lines_between = text_before[last_match.end():].count('\n')
            if lines_between <= 2:
                return self._clean_jsdoc(last_match.group(1))
        
        return None
    
    def _extract_jsdoc_before_in_text(self, text: str, position: int) -> Optional[str]:
        """Extract JSDoc comment before a position in given text."""
        text_before = text[:position]
        matches = list(self.JSDOC_PATTERN.finditer(text_before))
        
        if matches:
            last_match = matches[-1]
            lines_between = text_before[last_match.end():].count('\n')
            if lines_between <= 2:
                return self._clean_jsdoc(last_match.group(1))
        
        return None
    
    def _clean_jsdoc(self, jsdoc: str) -> str:
        """Clean JSDoc comment text."""
        lines = jsdoc.split('\n')
        cleaned = []
        
        for line in lines:
            line = line.strip()
            if line.startswith('*'):
                line = line[1:].strip()
            if line and not line.startswith('@'):
                cleaned.append(line)
        
        return ' '.join(cleaned)
    
    def _get_visibility(self, name: str) -> str:
        """Determine visibility from name."""
        if name.startswith('_'):
            return 'private'
        return 'public'
    
    def _empty_result(self) -> Dict[str, Any]:
        """Return empty result structure."""
        result = self.get_file_metadata()
        result.update({
            'language': 'typescript' if self.is_typescript else 'javascript',
            'classes': [],
            'functions': [],
            'imports': [],
            'documentation_coverage': 0.0,
        })
        return result

# Made with Bob
