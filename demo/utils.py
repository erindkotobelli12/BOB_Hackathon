"""Utility functions for data validation, transformation, and formatting.

This module provides a collection of commonly used utility functions for:
- Email validation using regex patterns
- Statistical calculations (averages)
- Dictionary operations (merging)
- CSV parsing
- Currency formatting with multi-currency support
- Duplicate detection in lists
"""

from typing import List, Dict, Union, Tuple
import re


def validate_email(email: str) -> bool:
    """Validate an email address using regex pattern matching.
    
    Checks if the provided string matches the standard email format:
    localpart@domain.tld where localpart can contain alphanumeric characters,
    dots, underscores, percent signs, plus and minus signs.
    
    Args:
        email (str): Email address string to validate
    
    Returns:
        bool: True if email matches valid format, False otherwise
    
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid.email")
        False
        >>> validate_email("user@domain.co.uk")
        True
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def calculate_average(numbers: List[Union[int, float]]) -> float:
    """Calculate the arithmetic mean of a list of numbers.
    
    Computes the average by summing all numbers and dividing by the count.
    
    Args:
        numbers (List[Union[int, float]]): List of numeric values to average
    
    Returns:
        float: The arithmetic mean of the input numbers
    
    Raises:
        ValueError: If the input list is empty
    
    Example:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([10.5, 20.5, 30.0])
        20.333333333333332
        >>> calculate_average([])
        Traceback (most recent call last):
        ValueError: Cannot calculate average of empty list
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def merge_dictionaries(dict1: Dict, dict2: Dict, overwrite: bool = True) -> Dict:
    """Merge two dictionaries with configurable overwrite behavior.
    
    Creates a new dictionary by combining dict1 and dict2. When keys overlap,
    the overwrite parameter controls whether dict2 values replace dict1 values.
    
    Args:
        dict1 (Dict): First dictionary (base)
        dict2 (Dict): Second dictionary (to merge in)
        overwrite (bool, optional): If True, dict2 values overwrite dict1 values
            for duplicate keys. If False, dict1 values are preserved.
            Defaults to True.
    
    Returns:
        Dict: New dictionary containing merged key-value pairs
    
    Example:
        >>> merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}
        >>> merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, overwrite=False)
        {'a': 1, 'b': 2, 'c': 4}
    
    Note:
        The original dictionaries are not modified; a new dictionary is returned.
    """
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and not overwrite:
            continue
        result[key] = value
    return result


def parse_csv_line(line: str, delimiter: str = ',') -> List[str]:
    """Parse a CSV line into a list of trimmed field values.
    
    Splits a string by the specified delimiter and strips whitespace from
    each resulting field.
    
    Args:
        line (str): CSV line string to parse
        delimiter (str, optional): Character(s) to split on. Defaults to ','.
    
    Returns:
        List[str]: List of trimmed field values
    
    Example:
        >>> parse_csv_line("apple, banana, cherry")
        ['apple', 'banana', 'cherry']
        >>> parse_csv_line("name|age|city", delimiter='|')
        ['name', 'age', 'city']
        >>> parse_csv_line("  spaces  ,  everywhere  ")
        ['spaces', 'everywhere']
    
    Note:
        This is a simple parser and does not handle quoted fields with
        embedded delimiters. For complex CSV parsing, use the csv module.
    """
    return [field.strip() for field in line.split(delimiter)]


def format_currency(amount: float, currency: str = 'USD') -> str:
    """Format a numeric amount as a currency string with symbol.
    
    Converts a float to a formatted currency string with thousands separators
    and two decimal places. Supports USD, EUR, and GBP with their respective
    symbols. Other currency codes are displayed as-is.
    
    Args:
        amount (float): Numeric amount to format
        currency (str, optional): Three-letter currency code (USD, EUR, GBP).
            Defaults to 'USD'.
    
    Returns:
        str: Formatted currency string with symbol and amount
    
    Example:
        >>> format_currency(1234.56)
        '$1,234.56'
        >>> format_currency(1000.00, 'EUR')
        '€1,000.00'
        >>> format_currency(999.99, 'GBP')
        '£999.99'
        >>> format_currency(500.00, 'JPY')
        'JPY500.00'
    """
    symbols = {'USD': '$', 'EUR': '€', 'GBP': '£'}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def find_duplicates(items: List[str]) -> Tuple[List[str], int]:
    """Find duplicate items in a list and return them with count.
    
    Identifies all items that appear more than once in the input list,
    preserving the order of first duplicate occurrence.
    
    Args:
        items (List[str]): List of strings to check for duplicates
    
    Returns:
        Tuple[List[str], int]: A tuple containing:
            - List of duplicate items (in order of first duplicate occurrence)
            - Count of total duplicate items found
    
    Example:
        >>> find_duplicates(['a', 'b', 'c', 'a', 'd', 'b'])
        (['a', 'b'], 2)
        >>> find_duplicates(['x', 'y', 'z'])
        ([], 0)
        >>> find_duplicates(['test', 'test', 'test'])
        (['test'], 1)
    
    Note:
        Each duplicate item appears only once in the returned list, even if
        it occurs multiple times in the input.
    """
    seen = set()
    duplicates = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates, len(duplicates)

# Made with Bob
