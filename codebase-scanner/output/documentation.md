# 📚 Documentation Report: demo

**Generated:** 2026-05-02 21:58:34 UTC
**Root Directory:** `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo`

## 📊 Coverage Summary

| Language | Files | Functions | Coverage % |
|----------|-------|-----------|------------|
| python | 4 | 20 | 80.0% |
| **Total** | **4** | **20** | **80.0%** |

## ⚠️ Undocumented Items

Found **4** undocumented functions/methods:

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\__init__.py`

- **timer** (function) - Line 6
- **memoize** (function) - Line 17
- **Singleton.__new__** (method) - Line 33
- **Singleton.clear_instances** (method) - Line 39

## 📄 File Documentation

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\__init__.py`

**Language:** python

#### Functions

##### `timer(func)`

**Line:** 6 | **Returns:** `Callable`

**Parameters:**
- `func` (Callable)

**Documentation:** _No documentation_

##### `memoize(func)`

**Line:** 17 | **Returns:** `Callable`

**Parameters:**
- `func` (Callable)

**Documentation:** _No documentation_

#### Classes

##### Class: `Singleton`

**Line:** 30

**Documentation:** _No documentation_

**Methods:**

- **`__new__(cls, *args, **kwargs)`** (Line 33)
  - Returns: `None`
  - _No documentation_

- **`clear_instances(cls)`** (Line 39)
  - Returns: `None`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\async_operations.py`

**Language:** python

#### Functions

##### `fetch_data(url, timeout)`

**Line:** 6 | **Returns:** `Dict`

**Parameters:**
- `url` (str)
- `timeout` (int)

**Documentation:**

> Fetch data from a URL asynchronously.
> 
> Args:
>     url: The URL to fetch data from
>     timeout: Request timeout in seconds
> 
> Returns:
>     Dictionary containing the JSON response

##### `process_batch(items, batch_size)`

**Line:** 23 | **Returns:** `List[str]`

**Parameters:**
- `items` (List[str])
- `batch_size` (int)

**Documentation:**

> Process items in batches asynchronously.
> 
> Args:
>     items: List of strings to process
>     batch_size: Number of items to process per batch
> 
> Returns:
>     List of processed strings in lowercase

##### `parallel_fetch(urls)`

**Line:** 43 | **Returns:** `List[Optional[Dict]]`

**Parameters:**
- `urls` (List[str])

**Documentation:**

> Fetch data from multiple URLs in parallel.
> 
> Args:
>     urls: List of URLs to fetch
> 
> Returns:
>     List of dictionaries or None for failed requests

##### `retry_operation(operation, max_retries, delay)`

**Line:** 58 | **Returns:** `Any`

**Parameters:**
- `operation` (Callable[[], Awaitable[Any]])
- `max_retries` (int)
- `delay` (float)

**Documentation:**

> Retry an async operation with exponential backoff.
> 
> Args:
>     operation: Async callable to retry
>     max_retries: Maximum number of retry attempts
>     delay: Base delay between retries in seconds
> 
> Returns:
>     Result of the operation
> 
> Raises:
>     Exception: If all retry attempts fail

##### `stream_processor(data_stream, callback)`

**Line:** 86 | **Returns:** `int`

**Parameters:**
- `data_stream` (AsyncIterator[Any])
- `callback` (Callable[[Any], Awaitable[None]])

**Documentation:**

> Process items from an async stream.
> 
> Args:
>     data_stream: Async iterator of items to process
>     callback: Async function to call for each item
> 
> Returns:
>     Total number of items processed

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\data_processor.py`

**Language:** python

#### Classes

##### Class: `DataProcessor`

**Line:** 11

**Documentation:**

> Process and transform text data with configuration management.
> 
> The DataProcessor class handles batch processing of string items, converting
> them to uppercase while optionally filtering empty entries. It maintains
> statistics about processed items and supports configuration export.
> 
> Attributes:
>     name (str): Identifier name for this processor instance
>     config (Dict): Configuration dictionary for processor settings
>     processed_count (int): Running count of total items processed
> 
> Example:
>     >>> processor = DataProcessor("main", {"batch_size": 100})
>     >>> result = processor.process_items(["hello", "world"])
>     >>> print(result)
>     ['HELLO', 'WORLD']

**Methods:**

- **`__init__(self, name, config)`** (Line 30)
  - Returns: `None`
  - Initialize a new DataProcessor instance.

- **`process_items(self, items, filter_empty)`** (Line 45)
  - Returns: `List[str]`
  - Process a list of string items by converting to uppercase.

- **`get_statistics(self)`** (Line 73)
  - Returns: `Dict[str, int]`
  - Get processing statistics for this processor instance.

- **`reset(self)`** (Line 93)
  - Returns: `None`
  - Reset the processed item counter to zero.

- **`export_config(self, filepath)`** (Line 108)
  - Returns: `bool`
  - Export the processor configuration to a JSON file.

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\utils.py`

**Language:** python

#### Functions

##### `validate_email(email)`

**Line:** 16 | **Returns:** `bool`

**Parameters:**
- `email` (str)

**Documentation:**

> Validate an email address using regex pattern matching.
> 
> Checks if the provided string matches the standard email format:
> localpart@domain.tld where localpart can contain alphanumeric characters,
> dots, underscores, percent signs, plus and minus signs.
> 
> Args:
>     email (str): Email address string to validate
> 
> Returns:
>     bool: True if email matches valid format, False otherwise
> 
> Example:
>     >>> validate_email("user@example.com")
>     True
>     >>> validate_email("invalid.email")
>     False
>     >>> validate_email("user@domain.co.uk")
>     True

##### `calculate_average(numbers)`

**Line:** 41 | **Returns:** `float`

**Parameters:**
- `numbers` (List[Union[int, float]])

**Documentation:**

> Calculate the arithmetic mean of a list of numbers.
> 
> Computes the average by summing all numbers and dividing by the count.
> 
> Args:
>     numbers (List[Union[int, float]]): List of numeric values to average
> 
> Returns:
>     float: The arithmetic mean of the input numbers
> 
> Raises:
>     ValueError: If the input list is empty
> 
> Example:
>     >>> calculate_average([1, 2, 3, 4, 5])
>     3.0
>     >>> calculate_average([10.5, 20.5, 30.0])
>     20.333333333333332
>     >>> calculate_average([])
>     Traceback (most recent call last):
>     ValueError: Cannot calculate average of empty list

##### `merge_dictionaries(dict1, dict2, overwrite)`

**Line:** 69 | **Returns:** `Dict`

**Parameters:**
- `dict1` (Dict)
- `dict2` (Dict)
- `overwrite` (bool)

**Documentation:**

> Merge two dictionaries with configurable overwrite behavior.
> 
> Creates a new dictionary by combining dict1 and dict2. When keys overlap,
> the overwrite parameter controls whether dict2 values replace dict1 values.
> 
> Args:
>     dict1 (Dict): First dictionary (base)
>     dict2 (Dict): Second dictionary (to merge in)
>     overwrite (bool, optional): If True, dict2 values overwrite dict1 values
>         for duplicate keys. If False, dict1 values are preserved.
>         Defaults to True.
> 
> Returns:
>     Dict: New dictionary containing merged key-value pairs
> 
> Example:
>     >>> merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
>     {'a': 1, 'b': 3, 'c': 4}
>     >>> merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, overwrite=False)
>     {'a': 1, 'b': 2, 'c': 4}
> 
> Note:
>     The original dictionaries are not modified; a new dictionary is returned.

##### `parse_csv_line(line, delimiter)`

**Line:** 102 | **Returns:** `List[str]`

**Parameters:**
- `line` (str)
- `delimiter` (str)

**Documentation:**

> Parse a CSV line into a list of trimmed field values.
> 
> Splits a string by the specified delimiter and strips whitespace from
> each resulting field.
> 
> Args:
>     line (str): CSV line string to parse
>     delimiter (str, optional): Character(s) to split on. Defaults to ','.
> 
> Returns:
>     List[str]: List of trimmed field values
> 
> Example:
>     >>> parse_csv_line("apple, banana, cherry")
>     ['apple', 'banana', 'cherry']
>     >>> parse_csv_line("name|age|city", delimiter='|')
>     ['name', 'age', 'city']
>     >>> parse_csv_line("  spaces  ,  everywhere  ")
>     ['spaces', 'everywhere']
> 
> Note:
>     This is a simple parser and does not handle quoted fields with
>     embedded delimiters. For complex CSV parsing, use the csv module.

##### `format_currency(amount, currency)`

**Line:** 130 | **Returns:** `str`

**Parameters:**
- `amount` (float)
- `currency` (str)

**Documentation:**

> Format a numeric amount as a currency string with symbol.
> 
> Converts a float to a formatted currency string with thousands separators
> and two decimal places. Supports USD, EUR, and GBP with their respective
> symbols. Other currency codes are displayed as-is.
> 
> Args:
>     amount (float): Numeric amount to format
>     currency (str, optional): Three-letter currency code (USD, EUR, GBP).
>         Defaults to 'USD'.
> 
> Returns:
>     str: Formatted currency string with symbol and amount
> 
> Example:
>     >>> format_currency(1234.56)
>     '$1,234.56'
>     >>> format_currency(1000.00, 'EUR')
>     '€1,000.00'
>     >>> format_currency(999.99, 'GBP')
>     '£999.99'
>     >>> format_currency(500.00, 'JPY')
>     'JPY500.00'

##### `find_duplicates(items)`

**Line:** 160 | **Returns:** `Tuple[List[str], int]`

**Parameters:**
- `items` (List[str])

**Documentation:**

> Find duplicate items in a list and return them with count.
> 
> Identifies all items that appear more than once in the input list,
> preserving the order of first duplicate occurrence.
> 
> Args:
>     items (List[str]): List of strings to check for duplicates
> 
> Returns:
>     Tuple[List[str], int]: A tuple containing:
>         - List of duplicate items (in order of first duplicate occurrence)
>         - Count of total duplicate items found
> 
> Example:
>     >>> find_duplicates(['a', 'b', 'c', 'a', 'd', 'b'])
>     (['a', 'b'], 2)
>     >>> find_duplicates(['x', 'y', 'z'])
>     ([], 0)
>     >>> find_duplicates(['test', 'test', 'test'])
>     (['test'], 1)
> 
> Note:
>     Each duplicate item appears only once in the returned list, even if
>     it occurs multiple times in the input.

---

## 📈 Summary Statistics

- **Total Files Scanned:** 4
- **Total Functions/Methods:** 20
- **Total Classes:** 2
- **Documentation Coverage:** 80.0%
- **Documented Items:** 16
- **Undocumented Items:** 4

---

_Generated by Codebase Scanner_