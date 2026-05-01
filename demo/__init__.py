from typing import Any, Callable
import functools
import time


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


def memoize(func: Callable) -> Callable:
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


class Singleton:
    _instances = {}
    
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]
    
    @classmethod
    def clear_instances(cls) -> None:
        cls._instances.clear()

# Made with Bob
