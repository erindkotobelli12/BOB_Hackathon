"""C/C++ parser using regex patterns."""

import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from .base_parser import BaseParser


class CppParser(BaseParser):
    """Parser for C and C++ source files."""
    
    # Regex patterns
    CLASS_PATTERN = re.compile(
        r'(?:class|struct)\s+(\w+)(?:\s*:\s*(?:public|private|protected)\s+([\w:]+))?',
        re.MULTILINE
    )
    FUNCTION_PATTERN = re.compile(
        r'(?:inline\s+)?(?:static\s+)?(?:virtual\s+)?([\w:<>*&\s]+)\s+(\w+)\s*\((.*?)\)(?:\s*const)?',
        re.MULTILINE | re.DOTALL
    )
    DOXYGEN_PATTERN = re.compile(
        r'/\*\*(.*?)\*/|///\s*(.*?)$',
        re.DOTALL | re.MULTILINE
    )
    INCLUDE_PATTERN = re.compile(
        r'#include\s+[<"].*?[>"]',
        re.MULTILINE
    )
    
    def __init__(self, file_path: Path):
        """
        Initialize C/C++ parser.
        
        Args:
            file_path: Path to C/C++ file
        """
        super().__init__(file_path)
        self.is_cpp = file_path.suffix in ['.cpp', '.cc', '.cxx', '.hpp', '.hh', '.hxx']
    
    def parse(self) -> Dict[str, Any]:
        """
        Parse C/C++ file and extract metadata.
        
        Returns:
            Dictionary containing classes, functions, imports, and coverage
        """
        if not self.load_file():
            return self._empty_result()
        
        classes = self._extract_classes() if self.is_cpp else []
        functions = self._extract_functions()
        includes = self._extract_includes()
        
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
            'language': 'cpp' if self.is_cpp else 'c',
            'classes': classes,
            'functions': functions,
            'imports': includes,
            'documentation_coverage': coverage,
        })
        
        return result
    
    def _extract_classes(self) -> List[Dict[str, Any]]:
        """Extract class/struct definitions (C++ only)."""
        classes = []
        
        for match in self.CLASS_PATTERN.finditer(self.content):
            class_name = match.group(1)
            base_class = match.group(2) if match.group(2) else None
            
            line_start = self.content[:match.start()].count('\n') + 1
            
            # Find class body
            class_start = match.end()
            brace_count = 0
            class_end = class_start
            found_brace = False
            
            for i, char in enumerate(self.content[class_start:], class_start):
                if char == '{':
                    found_brace = True
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0 and found_brace:
                        class_end = i
                        break
                elif char == ';' and not found_brace:
                    # Forward declaration
                    break
            
            if not found_brace:
                continue
            
            line_end = self.content[:class_end].count('\n') + 1
            class_body = self.content[class_start:class_end]
            
            # Extract Doxygen comment before class
            docstring = self._extract_doxygen_before(match.start())
            
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
        
        for match in self.FUNCTION_PATTERN.finditer(class_body):
            return_type = match.group(1).strip()
            method_name = match.group(2)
            params_str = match.group(3)
            
            # Skip common keywords and operators
            if method_name in ['if', 'for', 'while', 'switch', 'catch', 'return']:
                continue
            
            # Skip destructors and operators
            if method_name.startswith('~') or method_name.startswith('operator'):
                continue
            
            line_offset = class_body[:match.start()].count('\n')
            line_start = class_line_start + line_offset
            
            # Extract Doxygen comment
            docstring = self._extract_doxygen_before_in_text(class_body, match.start())
            
            # Determine visibility
            visibility = self._extract_visibility(class_body, match.start())
            
            methods.append({
                'name': method_name,
                'line_start': line_start,
                'line_end': line_start + 1,  # Approximate
                'parameters': self._parse_parameters(params_str),
                'return_type': return_type,
                'docstring': docstring,
                'decorators': [],
                'is_async': False,
                'visibility': visibility,
            })
        
        return methods
    
    def _extract_functions(self) -> List[Dict[str, Any]]:
        """Extract function definitions."""
        functions = []
        
        for match in self.FUNCTION_PATTERN.finditer(self.content):
            return_type = match.group(1).strip()
            func_name = match.group(2)
            params_str = match.group(3)
            
            # Skip common keywords
            if func_name in ['if', 'for', 'while', 'switch', 'catch', 'return', 'sizeof']:
                continue
            
            # Skip class methods (they're handled separately)
            # Simple heuristic: check if we're inside a class definition
            text_before = self.content[:match.start()]
            open_braces = text_before.count('{')
            close_braces = text_before.count('}')
            
            # If inside a class, skip (will be caught by method extraction)
            if open_braces > close_braces:
                # Check if there's a class/struct keyword before this
                last_class = max(
                    text_before.rfind('class '),
                    text_before.rfind('struct ')
                )
                if last_class > text_before.rfind('}'):
                    continue
            
            line_start = self.content[:match.start()].count('\n') + 1
            
            # Extract Doxygen comment
            docstring = self._extract_doxygen_before(match.start())
            
            functions.append({
                'name': func_name,
                'line_start': line_start,
                'line_end': line_start + 1,  # Approximate
                'parameters': self._parse_parameters(params_str),
                'return_type': return_type,
                'docstring': docstring,
                'decorators': [],
                'is_async': False,
            })
        
        return functions
    
    def _parse_parameters(self, params_str: str) -> List[Dict[str, Any]]:
        """Parse function parameters."""
        if not params_str.strip() or params_str.strip() == 'void':
            return []
        
        params = []
        # Split by comma
        for param in params_str.split(','):
            param = param.strip()
            if not param:
                continue
            
            # Parse type and name
            # Format: [const] Type [*&] name [= default]
            parts = param.split('=')
            param_decl = parts[0].strip()
            default = parts[1].strip() if len(parts) > 1 else None
            
            # Extract name (last word) and type (everything else)
            words = param_decl.split()
            if words:
                param_name = words[-1].strip('*&')
                param_type = ' '.join(words[:-1]) if len(words) > 1 else 'unknown'
                
                params.append({
                    'name': param_name,
                    'type': param_type,
                    'default': default,
                })
        
        return params
    
    def _extract_includes(self) -> List[str]:
        """Extract include statements."""
        includes = []
        
        for match in self.INCLUDE_PATTERN.finditer(self.content):
            includes.append(match.group(0).strip())
        
        return includes
    
    def _extract_doxygen_before(self, position: int) -> Optional[str]:
        """Extract Doxygen comment before a position."""
        text_before = self.content[:position]
        
        # Look for /** */ style comments
        block_matches = list(re.finditer(r'/\*\*(.*?)\*/', text_before, re.DOTALL))
        if block_matches:
            last_match = block_matches[-1]
            lines_between = text_before[last_match.end():].count('\n')
            if lines_between <= 2:
                return self._clean_doxygen(last_match.group(1))
        
        # Look for /// style comments
        lines = text_before.split('\n')
        comment_lines = []
        for line in reversed(lines[-5:]):  # Check last 5 lines
            stripped = line.strip()
            if stripped.startswith('///'):
                comment_lines.insert(0, stripped[3:].strip())
            elif stripped and not stripped.startswith('//'):
                break
        
        if comment_lines:
            return ' '.join(comment_lines)
        
        return None
    
    def _extract_doxygen_before_in_text(self, text: str, position: int) -> Optional[str]:
        """Extract Doxygen comment before a position in given text."""
        text_before = text[:position]
        
        block_matches = list(re.finditer(r'/\*\*(.*?)\*/', text_before, re.DOTALL))
        if block_matches:
            last_match = block_matches[-1]
            lines_between = text_before[last_match.end():].count('\n')
            if lines_between <= 2:
                return self._clean_doxygen(last_match.group(1))
        
        return None
    
    def _clean_doxygen(self, doxygen: str) -> str:
        """Clean Doxygen comment text."""
        lines = doxygen.split('\n')
        cleaned = []
        
        for line in lines:
            line = line.strip()
            if line.startswith('*'):
                line = line[1:].strip()
            if line and not line.startswith('@') and not line.startswith('\\'):
                cleaned.append(line)
        
        return ' '.join(cleaned)
    
    def _extract_visibility(self, text: str, position: int) -> str:
        """Extract visibility modifier from class body."""
        # Look backwards for visibility keywords
        text_before = text[:position]
        last_public = text_before.rfind('public:')
        last_private = text_before.rfind('private:')
        last_protected = text_before.rfind('protected:')
        
        max_pos = max(last_public, last_private, last_protected)
        
        if max_pos == last_private:
            return 'private'
        elif max_pos == last_protected:
            return 'protected'
        elif max_pos == last_public:
            return 'public'
        
        return 'private'  # Default for class
    
    def _empty_result(self) -> Dict[str, Any]:
        """Return empty result structure."""
        result = self.get_file_metadata()
        result.update({
            'language': 'cpp' if self.is_cpp else 'c',
            'classes': [],
            'functions': [],
            'imports': [],
            'documentation_coverage': 0.0,
        })
        return result

# Made with Bob
