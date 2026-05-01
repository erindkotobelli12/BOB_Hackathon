"""JavaScript/TypeScript parser using regex patterns."""

import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from .base_parser import BaseParser


class JavaScriptParser(BaseParser):
    """Parser for JavaScript and TypeScript files."""
    
    # Regex patterns for parsing
    CLASS_PATTERN = re.compile(
        r'(?:export\s+)?(?:default\s+)?class\s+(\w+)(?:<[^>]+>)?(?:\s+extends\s+([\w.]+)(?:<[^>]+>)?)?',
        re.MULTILINE
    )
    FUNCTION_PATTERN = re.compile(
        r'(?:export\s+)?(?:async\s+)?function\s+(\w+)(?:<[^>]+>)?\s*\((.*?)\)(?:\s*:\s*([\w<>[\]|,\s]+))?',
        re.MULTILINE | re.DOTALL
    )
    # Improved arrow function pattern to handle various formats
    ARROW_FUNCTION_PATTERN = re.compile(
        r'(?:export\s+)?(?:const|let|var)\s+(\w+)\s*(?::\s*[\w<>[\]|,\s()=>]+)?\s*=\s*(?:async\s+)?\((.*?)\)(?:\s*:\s*([\w<>[\]|,\s]+))?\s*=>',
        re.MULTILINE | re.DOTALL
    )
    # Pattern for class property arrow functions
    CLASS_PROPERTY_ARROW_PATTERN = re.compile(
        r'(?:(public|private|protected|readonly)\s+)?(\w+)\s*(?::\s*[\w<>[\]|,\s()=>]+)?\s*=\s*(?:async\s+)?\((.*?)\)(?:\s*:\s*([\w<>[\]|,\s]+))?\s*=>',
        re.MULTILINE | re.DOTALL
    )
    # Improved method pattern with TypeScript access modifiers
    METHOD_PATTERN = re.compile(
        r'(?:(public|private|protected|readonly|static)\s+)?(?:async\s+)?(\w+)(?:<[^>]+>)?\s*\((.*?)\)(?:\s*:\s*([\w<>[\]|,\s]+))?\s*\{',
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
        
        # Extract regular methods with TypeScript access modifiers
        for match in self.METHOD_PATTERN.finditer(class_body):
            access_modifier = match.group(1)
            method_name = match.group(2)
            
            # Skip constructor and common non-methods
            if method_name in ['if', 'for', 'while', 'switch', 'catch']:
                continue
            
            params_str = match.group(3)
            return_type = match.group(4)
            
            line_offset = class_body[:match.start()].count('\n')
            line_start = class_line_start + line_offset
            
            # Extract JSDoc
            docstring = self._extract_jsdoc_before_in_text(class_body, match.start())
            
            # Determine visibility from access modifier or name
            visibility = self._get_visibility_from_modifier(access_modifier, method_name)
            
            methods.append({
                'name': method_name,
                'line_start': line_start,
                'line_end': line_start + 1,  # Approximate
                'parameters': self._parse_parameters(params_str),
                'return_type': return_type,
                'docstring': docstring,
                'decorators': [],
                'is_async': 'async' in class_body[max(0, match.start()-20):match.start()],
                'visibility': visibility,
                'is_static': access_modifier == 'static' if access_modifier else False,
            })
        
        # Extract class property arrow functions
        for match in self.CLASS_PROPERTY_ARROW_PATTERN.finditer(class_body):
            access_modifier = match.group(1)
            method_name = match.group(2)
            params_str = match.group(3)
            return_type = match.group(4)
            
            line_offset = class_body[:match.start()].count('\n')
            line_start = class_line_start + line_offset
            
            # Extract JSDoc
            docstring = self._extract_jsdoc_before_in_text(class_body, match.start())
            
            # Determine visibility from access modifier or name
            visibility = self._get_visibility_from_modifier(access_modifier, method_name)
            
            # Check for async in the matched text
            matched_text = match.group(0)
            is_async = 'async' in matched_text
            
            methods.append({
                'name': method_name,
                'line_start': line_start,
                'line_end': line_start + 1,  # Approximate
                'parameters': self._parse_parameters(params_str),
                'return_type': return_type,
                'docstring': docstring,
                'decorators': [],
                'is_async': is_async,
                'visibility': visibility,
                'is_arrow_function': True,
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
            return_type = match.group(3).strip() if match.group(3) else None
            line_start = self.content[:match.start()].count('\n') + 1
            
            docstring = self._extract_jsdoc_before(match.start())
            
            # Check for async in the matched text
            matched_text = match.group(0)
            is_async = 'async' in matched_text
            
            functions.append({
                'name': func_name,
                'line_start': line_start,
                'line_end': line_start + 1,  # Approximate
                'parameters': self._parse_parameters(params_str),
                'return_type': return_type,
                'docstring': docstring,
                'decorators': [],
                'is_async': is_async,
            })
        
        return functions
    
    def _parse_parameters(self, params_str: str) -> List[Dict[str, Any]]:
        """Parse function parameters."""
        if not params_str.strip():
            return []
        
        params = []
        # Smart split by comma that respects nested brackets and parentheses
        current_param = []
        depth = 0
        in_string = False
        string_char = None
        
        for char in params_str:
            if char in ['"', "'", '`'] and not in_string:
                in_string = True
                string_char = char
            elif in_string and char == string_char:
                in_string = False
                string_char = None
            elif not in_string:
                if char in ['<', '(', '[', '{']:
                    depth += 1
                elif char in ['>', ')', ']', '}']:
                    depth -= 1
                elif char == ',' and depth == 0:
                    params.append(self._parse_single_parameter(''.join(current_param)))
                    current_param = []
                    continue
            
            current_param.append(char)
        
        # Add the last parameter
        if current_param:
            params.append(self._parse_single_parameter(''.join(current_param)))
        
        return params
    
    def _parse_single_parameter(self, param: str) -> Dict[str, Any]:
        """Parse a single parameter string."""
        param = param.strip()
        if not param:
            return {'name': '', 'type': None, 'default': None}
        
        name = param
        param_type = None
        default = None
        
        # Check for default value (but not in type annotations)
        # Find the last '=' that's not inside brackets
        depth = 0
        equal_pos = -1
        for i, char in enumerate(param):
            if char in ['<', '(', '[', '{']:
                depth += 1
            elif char in ['>', ')', ']', '}']:
                depth -= 1
            elif char == '=' and depth == 0:
                equal_pos = i
        
        if equal_pos > 0:
            default = param[equal_pos + 1:].strip()
            param = param[:equal_pos].strip()
        
        # Check for type annotation
        # Find the first ':' that's not inside brackets
        depth = 0
        colon_pos = -1
        for i, char in enumerate(param):
            if char in ['<', '(', '[', '{']:
                depth += 1
            elif char in ['>', ')', ']', '}']:
                depth -= 1
            elif char == ':' and depth == 0:
                colon_pos = i
                break
        
        if colon_pos > 0:
            name = param[:colon_pos].strip()
            param_type = param[colon_pos + 1:].strip()
        else:
            name = param
        
        # Remove optional marker '?' from name
        if name.endswith('?'):
            name = name[:-1].strip()
        
        return {
            'name': name,
            'type': param_type,
            'default': default,
        }
    
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
    
    def _get_visibility_from_modifier(self, modifier: Optional[str], name: str) -> str:
        """
        Determine visibility from TypeScript access modifier or name.
        
        Args:
            modifier: TypeScript access modifier (public, private, protected, readonly, static)
            name: Method or property name
        
        Returns:
            Visibility string (public, private, or protected)
        """
        if modifier in ['private', 'protected', 'public']:
            return modifier
        # Fall back to name-based detection
        return self._get_visibility(name)
    
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
