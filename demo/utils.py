from typing import List, Dict, Union, Tuple
import re


def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def calculate_average(numbers: List[Union[int, float]]) -> float:
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def merge_dictionaries(dict1: Dict, dict2: Dict, overwrite: bool = True) -> Dict:
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and not overwrite:
            continue
        result[key] = value
    return result


def parse_csv_line(line: str, delimiter: str = ',') -> List[str]:
    return [field.strip() for field in line.split(delimiter)]


def format_currency(amount: float, currency: str = 'USD') -> str:
    symbols = {'USD': '$', 'EUR': '€', 'GBP': '£'}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def find_duplicates(items: List[str]) -> Tuple[List[str], int]:
    seen = set()
    duplicates = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates, len(duplicates)

# Made with Bob
