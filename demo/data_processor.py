"""Data processing module for transforming and managing text data.

This module provides the DataProcessor class for batch processing of string items
with configurable settings and statistics tracking.
"""

from typing import List, Dict, Optional
import json


class DataProcessor:
    """Process and transform text data with configuration management.
    
    The DataProcessor class handles batch processing of string items, converting
    them to uppercase while optionally filtering empty entries. It maintains
    statistics about processed items and supports configuration export.
    
    Attributes:
        name (str): Identifier name for this processor instance
        config (Dict): Configuration dictionary for processor settings
        processed_count (int): Running count of total items processed
    
    Example:
        >>> processor = DataProcessor("main", {"batch_size": 100})
        >>> result = processor.process_items(["hello", "world"])
        >>> print(result)
        ['HELLO', 'WORLD']
    """
    
    def __init__(self, name: str, config: Optional[Dict] = None):
        """Initialize a new DataProcessor instance.
        
        Args:
            name (str): Unique identifier name for this processor
            config (Optional[Dict], optional): Configuration dictionary containing
                processor settings. Defaults to None (empty dict).
        
        Example:
            >>> processor = DataProcessor("batch_processor", {"timeout": 30})
        """
        self.name = name
        self.config = config or {}
        self.processed_count = 0
    
    def process_items(self, items: List[str], filter_empty: bool = True) -> List[str]:
        """Process a list of string items by converting to uppercase.
        
        Transforms all input strings to uppercase and optionally filters out
        empty or whitespace-only strings. Updates the internal processed count.
        
        Args:
            items (List[str]): List of string items to process
            filter_empty (bool, optional): If True, removes empty/whitespace-only
                strings before processing. Defaults to True.
        
        Returns:
            List[str]: List of processed strings in uppercase
        
        Example:
            >>> processor = DataProcessor("test")
            >>> processor.process_items(["hello", "", "world"], filter_empty=True)
            ['HELLO', 'WORLD']
            >>> processor.process_items(["hello", "", "world"], filter_empty=False)
            ['HELLO', '', 'WORLD']
        """
        if filter_empty:
            items = [item for item in items if item.strip()]
        
        processed = [item.upper() for item in items]
        self.processed_count += len(processed)
        return processed
    
    def get_statistics(self) -> Dict[str, int]:
        """Get processing statistics for this processor instance.
        
        Returns:
            Dict[str, int]: Dictionary containing:
                - 'total_processed': Total number of items processed
                - 'config_keys': Number of configuration keys set
        
        Example:
            >>> processor = DataProcessor("test", {"key1": "value1"})
            >>> processor.process_items(["a", "b", "c"])
            >>> stats = processor.get_statistics()
            >>> print(stats)
            {'total_processed': 3, 'config_keys': 1}
        """
        return {
            'total_processed': self.processed_count,
            'config_keys': len(self.config)
        }
    
    def reset(self) -> None:
        """Reset the processed item counter to zero.
        
        Clears the internal count of processed items while preserving
        the configuration and processor name.
        
        Example:
            >>> processor = DataProcessor("test")
            >>> processor.process_items(["a", "b"])
            >>> processor.reset()
            >>> processor.get_statistics()['total_processed']
            0
        """
        self.processed_count = 0
    
    def export_config(self, filepath: str) -> bool:
        """Export the processor configuration to a JSON file.
        
        Writes the current configuration dictionary to a JSON file with
        pretty-printing (2-space indentation).
        
        Args:
            filepath (str): Path to the output JSON file
        
        Returns:
            bool: True if export succeeded, False if an error occurred
        
        Example:
            >>> processor = DataProcessor("test", {"timeout": 30})
            >>> success = processor.export_config("config.json")
            >>> print(success)
            True
        
        Note:
            Errors are printed to stdout but do not raise exceptions.
        """
        try:
            with open(filepath, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting config: {e}")
            return False

# Made with Bob
