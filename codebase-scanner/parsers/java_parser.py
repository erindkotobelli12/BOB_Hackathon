"""Java parser using regex patterns."""

import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from .base_parser import BaseParser


class JavaParser(BaseParser):
    """Parser for Java source files."""
    
    # Regex patterns
    CLASS_PATTERN = re.compile(
        r'(?:public|private|protected)?\s*(?:static)?\s*(?:final)?\s*(?:abstract)?\s*class\s+(\w+)(?:\s+extends\s+([\w.]+))?(?:\s+implements\s+([\w.,\s]+))?',
        re.MULTILINE
    )
    METHOD_PATTERN = re.compile(
        r'(?:public|private|protected)?\s*(?:static)?\s*(?:final)?\s*(?:synchronized)?\s*([\w<>[\]]+)\s+(\w+)\s*\((.*?)\)',
        re.MULTILINE | re.DOTALL
    )
    JAVADOC_PATTERN = re.compile(
        r'/\*\*(.*?)\*/',
        re.DOTALL
    )
    IMPORT_PATTERN = re.compile(
        r'import\s+[\w.]+;',
        re.MULTILINE
    )
    
    def __init__(self, file_path: Path):
        """
        Initialize Java parser.
        
        Args:
            file_path: Path to Java file
        """
        super().__init__(file_path)
    
    def parse(self) -> Dict[str, Any]:
        """
        Parse Java file and extract metadata.
        
        Returns:
            Dictionary containing classes, functions, imports, and coverage
        """
        if not self.load_file():
            return self._empty_result()
        
        classes = self._extract_classes()
        imports = self._extract_imports()
        
        # Calculate documentation coverage
        total_items = sum(len(cls['methods']) for cls in classes)
        documented_items = sum(
            1 for cls in classes for m in cls['methods'] if m.get('docstring')
        )
        
        coverage = self.calculate_coverage(documented_items, total_items)
        
        result = self.get_file_metadata()
        result.update({
            'language': 'java',
            'classes': classes,
            'functions': [],  # Java doesn't have top-level functions
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
            interfaces = match.group(3).split(',') if match.group(3) else []
            interfaces = [i.strip() for i in interfaces]
            
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
            
            # Extract Javadoc before class
            docstring = self._extract_javadoc_before(match.start())
            
            # Extract methods
            methods = self._extract_methods(class_body, line_start)
            
            base_classes = [base_class] if base_class else []
            base_classes.extend(interfaces)
            
            classes.append({
                'name': class_name,
                'line_start': line_start,
                'line_end': line_end,
                'docstring': docstring,
                'methods': methods,
                'base_classes': base_classes,
                'decorators': [],
            })
        
        return classes
    
    def _extract_methods(self, class_body: str, class_line_start: int) -> List[Dict[str, Any]]:
        """Extract method definitions from class body."""
        methods = []
        
        for match in self.METHOD_PATTERN.finditer(class_body):
            return_type = match.group(1)
            method_name = match.group(2)
            params_str = match.group(3)
            
            # Skip common keywords that might match
            if method_name in ['if', 'for', 'while', 'switch', 'catch', 'synchronized']:
                continue
            
            line_offset = class_body[:match.start()].count('\n')
            line_start = class_line_start + line_offset
            
            # Extract Javadoc
            docstring = self._extract_javadoc_before_in_text(class_body, match.start())
            
            # Determine visibility
            visibility = self._extract_visibility(class_body[max(0, match.start()-50):match.start()])
            
            methods.append({
                'name': method_name,
                'line_start': line_start,
                'line_end': line_start + 1,  # Approximate
                'parameters': self._parse_parameters(params_str),
                'return_type': return_type,
                'docstring': docstring,
                'decorators': self._extract_annotations(class_body, match.start()),
                'is_async': False,  # Java doesn't have async keyword
                'visibility': visibility,
            })
        
        return methods
    
    def _parse_parameters(self, params_str: str) -> List[Dict[str, Any]]:
        """Parse method parameters."""
        if not params_str.strip():
            return []
        
        params = []
        # Split by comma, but be careful with generics
        current_param = ""
        angle_bracket_count = 0
        
        for char in params_str + ',':
            if char == '<':
                angle_bracket_count += 1
                current_param += char
            elif char == '>':
                angle_bracket_count -= 1
                current_param += char
            elif char == ',' and angle_bracket_count == 0:
                if current_param.strip():
                    params.append(self._parse_single_parameter(current_param.strip()))
                current_param = ""
            else:
                current_param += char
        
        return params
    
    def _parse_single_parameter(self, param: str) -> Dict[str, Any]:
        """Parse a single parameter."""
        # Format: [final] Type name [= default]
        parts = param.split()
        
        if len(parts) >= 2:
            # Remove 'final' if present
            if parts[0] == 'final':
                parts = parts[1:]
            
            param_type = parts[0]
            param_name = parts[1]
            
            # Handle varargs
            if '...' in param_type:
                param_type = param_type.replace('...', '[]')
            
            return {
                'name': param_name,
                'type': param_type,
                'default': None,
            }
        
        return {
            'name': param,
            'type': None,
            'default': None,
        }
    
    def _extract_imports(self) -> List[str]:
        """Extract import statements."""
        imports = []
        
        for match in self.IMPORT_PATTERN.finditer(self.content):
            imports.append(match.group(0).strip())
        
        return imports
    
    def _extract_javadoc_before(self, position: int) -> Optional[str]:
        """Extract Javadoc comment before a position."""
        text_before = self.content[:position]
        matches = list(self.JAVADOC_PATTERN.finditer(text_before))
        
        if matches:
            last_match = matches[-1]
            lines_between = text_before[last_match.end():].count('\n')
            if lines_between <= 2:
                return self._clean_javadoc(last_match.group(1))
        
        return None
    
    def _extract_javadoc_before_in_text(self, text: str, position: int) -> Optional[str]:
        """Extract Javadoc comment before a position in given text."""
        text_before = text[:position]
        matches = list(self.JAVADOC_PATTERN.finditer(text_before))
        
        if matches:
            last_match = matches[-1]
            lines_between = text_before[last_match.end():].count('\n')
            if lines_between <= 2:
                return self._clean_javadoc(last_match.group(1))
        
        return None
    
    def _clean_javadoc(self, javadoc: str) -> str:
        """Clean Javadoc comment text."""
        lines = javadoc.split('\n')
        cleaned = []
        
        for line in lines:
            line = line.strip()
            if line.startswith('*'):
                line = line[1:].strip()
            if line and not line.startswith('@'):
                cleaned.append(line)
        
        return ' '.join(cleaned)
    
    def _extract_visibility(self, text: str) -> str:
        """Extract visibility modifier."""
        if 'private' in text:
            return 'private'
        elif 'protected' in text:
            return 'protected'
        elif 'public' in text:
            return 'public'
        return 'package'  # Default in Java
    
    def _extract_annotations(self, text: str, position: int) -> List[str]:
        """Extract annotations before a method."""
        annotations = []
        text_before = text[max(0, position-200):position]
        
        # Find annotations like @Override, @Deprecated, etc.
        annotation_pattern = re.compile(r'@(\w+)(?:\([^)]*\))?')
        for match in annotation_pattern.finditer(text_before):
            annotations.append(f"@{match.group(1)}")
        
        return annotations
    
    def _empty_result(self) -> Dict[str, Any]:
        """Return empty result structure."""
        result = self.get_file_metadata()
        result.update({
            'language': 'java',
            'classes': [],
            'functions': [],
            'imports': [],
            'documentation_coverage': 0.0,
        })
        return result

# Made with Bob
