# 📚 Documentation Report: demo

**Generated:** 2026-05-01 16:35:05 UTC
**Root Directory:** `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo`

## 📊 Coverage Summary

| Language | Files | Functions | Coverage % |
|----------|-------|-----------|------------|
| python | 4 | 20 | 0.0% |
| **Total** | **4** | **20** | **0.0%** |

## ⚠️ Undocumented Items

Found **20** undocumented functions/methods:

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\__init__.py`

- **timer** (function) - Line 6
- **memoize** (function) - Line 17
- **Singleton.__new__** (method) - Line 33
- **Singleton.clear_instances** (method) - Line 39

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\async_operations.py`

- **fetch_data** (function) - Line 6
- **process_batch** (function) - Line 12
- **parallel_fetch** (function) - Line 22
- **retry_operation** (function) - Line 28
- **stream_processor** (function) - Line 38

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\data_processor.py`

- **DataProcessor.__init__** (method) - Line 6
- **DataProcessor.process_items** (method) - Line 11
- **DataProcessor.get_statistics** (method) - Line 19
- **DataProcessor.reset** (method) - Line 25
- **DataProcessor.export_config** (method) - Line 28

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\utils.py`

- **validate_email** (function) - Line 5
- **calculate_average** (function) - Line 10
- **merge_dictionaries** (function) - Line 16
- **parse_csv_line** (function) - Line 25
- **format_currency** (function) - Line 29
- **find_duplicates** (function) - Line 35

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

**Documentation:** _No documentation_

##### `process_batch(items, batch_size)`

**Line:** 12 | **Returns:** `List[str]`

**Parameters:**
- `items` (List[str])
- `batch_size` (int)

**Documentation:** _No documentation_

##### `parallel_fetch(urls)`

**Line:** 22 | **Returns:** `List[Optional[Dict]]`

**Parameters:**
- `urls` (List[str])

**Documentation:** _No documentation_

##### `retry_operation(operation, max_retries, delay)`

**Line:** 28 | **Returns:** `None`

**Parameters:**
- `operation`
- `max_retries` (int)
- `delay` (float)

**Documentation:** _No documentation_

##### `stream_processor(data_stream, callback)`

**Line:** 38 | **Returns:** `int`

**Parameters:**
- `data_stream`
- `callback`

**Documentation:** _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\data_processor.py`

**Language:** python

#### Classes

##### Class: `DataProcessor`

**Line:** 5

**Documentation:** _No documentation_

**Methods:**

- **`__init__(self, name, config)`** (Line 6)
  - Returns: `None`
  - _No documentation_

- **`process_items(self, items, filter_empty)`** (Line 11)
  - Returns: `List[str]`
  - _No documentation_

- **`get_statistics(self)`** (Line 19)
  - Returns: `Dict[str, int]`
  - _No documentation_

- **`reset(self)`** (Line 25)
  - Returns: `None`
  - _No documentation_

- **`export_config(self, filepath)`** (Line 28)
  - Returns: `bool`
  - _No documentation_

---

### `C:\Users\I.C.T\OneDrive\Documents\git\BOB_Hackathon\demo\utils.py`

**Language:** python

#### Functions

##### `validate_email(email)`

**Line:** 5 | **Returns:** `bool`

**Parameters:**
- `email` (str)

**Documentation:** _No documentation_

##### `calculate_average(numbers)`

**Line:** 10 | **Returns:** `float`

**Parameters:**
- `numbers` (List[Union[int, float]])

**Documentation:** _No documentation_

##### `merge_dictionaries(dict1, dict2, overwrite)`

**Line:** 16 | **Returns:** `Dict`

**Parameters:**
- `dict1` (Dict)
- `dict2` (Dict)
- `overwrite` (bool)

**Documentation:** _No documentation_

##### `parse_csv_line(line, delimiter)`

**Line:** 25 | **Returns:** `List[str]`

**Parameters:**
- `line` (str)
- `delimiter` (str)

**Documentation:** _No documentation_

##### `format_currency(amount, currency)`

**Line:** 29 | **Returns:** `str`

**Parameters:**
- `amount` (float)
- `currency` (str)

**Documentation:** _No documentation_

##### `find_duplicates(items)`

**Line:** 35 | **Returns:** `Tuple[List[str], int]`

**Parameters:**
- `items` (List[str])

**Documentation:** _No documentation_

---

## 📈 Summary Statistics

- **Total Files Scanned:** 4
- **Total Functions/Methods:** 20
- **Total Classes:** 2
- **Documentation Coverage:** 0.0%
- **Documented Items:** 0
- **Undocumented Items:** 20

---

_Generated by Codebase Scanner_