"""Python documentation writer using watsonx.ai for Google-style docstrings."""

from pathlib import Path
from typing import Dict, List, Any, Optional
from .watsonx_client import WatsonxClient


class PythonDocWriter:
    """Generate and manage Python docstrings using AI."""
    
    def __init__(self, dry_run: bool = False):
        """Initialize Python doc writer with watsonx client."""
        self.client = WatsonxClient(dry_run=dry_run)
        self.dry_run = dry_run
    
    def generate_for_file(self, file_path: Path, file_content: str, 
                         functions: List[Dict[str, Any]], 
                         classes: List[Dict[str, Any]]) -> Dict[str, str]:
        """
        Generate docstrings for all undocumented items in a file.
        
        Args:
            file_path: Path to the Python file
            file_content: Full content of the file
            functions: List of function metadata from parser
            classes: List of class metadata from parser
            
        Returns:
            Dict mapping function/class names to generated docstrings
        """
        docstrings = {}
        
        # Generate for top-level functions
        for func in functions:
            if not func.get('docstring'):
                docstring = self._generate_function_doc(file_content, func)
                if docstring:
                    docstrings[func['name']] = docstring
        
        # Generate for classes and their methods
        for cls in classes:
            if not cls.get('docstring'):
                docstring = self._generate_class_doc(file_content, cls)
                if docstring:
                    docstrings[cls['name']] = docstring
            
            # Generate for undocumented methods
            for method in cls.get('methods', []):
                if not method.get('docstring'):
                    docstring = self._generate_method_doc(file_content, method, cls['name'])
                    if docstring:
                        docstrings[method['name']] = docstring
        
        return docstrings
    
    def _generate_function_doc(self, file_content: str, func: Dict[str, Any]) -> Optional[str]:
        """Generate docstring for a function."""
        signature = self._extract_signature(file_content, func)
        body = self._extract_body(file_content, func)
        
        if not signature or not body:
            return None
        
        return self.client.generate_docstring(signature, body)
    
    def _generate_method_doc(self, file_content: str, method: Dict[str, Any], 
                            class_name: str) -> Optional[str]:
        """Generate docstring for a method."""
        return self._generate_function_doc(file_content, method)
    
    def _generate_class_doc(self, file_content: str, cls: Dict[str, Any]) -> Optional[str]:
        """Generate docstring for a class."""
        lines = file_content.split('\n')
        start = cls['line_start'] - 1
        
        # Get class signature
        signature_lines = []
        for i in range(start, min(start + 5, len(lines))):
            signature_lines.append(lines[i])
            if ':' in lines[i]:
                break
        
        signature = '\n'.join(signature_lines)
        
        # Get class body (first few lines)
        body_lines = []
        for i in range(start + len(signature_lines), min(start + 20, len(lines))):
            body_lines.append(lines[i])
        
        body = '\n'.join(body_lines)
        
        return self.client.generate_docstring(signature, body)
    
    def _extract_signature(self, file_content: str, func: Dict[str, Any]) -> str:
        """Extract function signature from file content."""
        lines = file_content.split('\n')
        start = func['line_start'] - 1
        
        # Get signature (may span multiple lines)
        signature_lines = []
        for i in range(start, min(start + 10, len(lines))):
            signature_lines.append(lines[i])
            if ':' in lines[i]:
                break
        
        return '\n'.join(signature_lines)
    
    def _extract_body(self, file_content: str, func: Dict[str, Any]) -> str:
        """Extract function body from file content."""
        lines = file_content.split('\n')
        start = func['line_start'] - 1
        end = func.get('line_end', start + 20)
        
        # Skip signature lines
        body_start = start
        for i in range(start, min(start + 10, len(lines))):
            if ':' in lines[i]:
                body_start = i + 1
                break
        
        # Get body (limit to reasonable size)
        body_lines = lines[body_start:min(end, body_start + 30)]
        return '\n'.join(body_lines)


def generate_docstrings_for_files(files_data: List[Dict[str, Any]], dry_run: bool = False) -> Dict[Path, Dict[str, str]]:
    """
    Generate docstrings for multiple Python files.
    
    Args:
        files_data: List of file metadata from scanner
        dry_run: If True, only show what would be documented without API calls
        
    Returns:
        Dict mapping file paths to docstring dicts
    """
    writer = PythonDocWriter(dry_run=dry_run)
    results = {}
    
    for file_data in files_data:
        if file_data.get('language') != 'python':
            continue
        
        file_path = Path(file_data['path'])
        
        # Read file content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
        
        # Generate docstrings
        docstrings = writer.generate_for_file(
            file_path,
            content,
            file_data.get('functions', []),
            file_data.get('classes', [])
        )
        
        if docstrings:
            results[file_path] = docstrings
    
    return results

# Made with Bob
