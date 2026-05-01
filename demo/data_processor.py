from typing import List, Dict, Optional
import json


class DataProcessor:
    def __init__(self, name: str, config: Optional[Dict] = None):
        self.name = name
        self.config = config or {}
        self.processed_count = 0
    
    def process_items(self, items: List[str], filter_empty: bool = True) -> List[str]:
        if filter_empty:
            items = [item for item in items if item.strip()]
        
        processed = [item.upper() for item in items]
        self.processed_count += len(processed)
        return processed
    
    def get_statistics(self) -> Dict[str, int]:
        return {
            'total_processed': self.processed_count,
            'config_keys': len(self.config)
        }
    
    def reset(self) -> None:
        self.processed_count = 0
    
    def export_config(self, filepath: str) -> bool:
        try:
            with open(filepath, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting config: {e}")
            return False

# Made with Bob
