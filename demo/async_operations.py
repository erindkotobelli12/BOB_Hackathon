import asyncio
from typing import List, Dict, Optional, Callable, Any, AsyncIterator, Awaitable
import aiohttp


async def fetch_data(url: str, timeout: int = 30) -> Dict:
    """
    Fetch data from a URL asynchronously.
    
    Args:
        url: The URL to fetch data from
        timeout: Request timeout in seconds
    
    Returns:
        Dictionary containing the JSON response
    """
    timeout_obj = aiohttp.ClientTimeout(total=timeout)
    async with aiohttp.ClientSession(timeout=timeout_obj) as session:
        async with session.get(url) as response:
            return await response.json()


async def process_batch(items: List[str], batch_size: int = 10) -> List[str]:
    """
    Process items in batches asynchronously.
    
    Args:
        items: List of strings to process
        batch_size: Number of items to process per batch
    
    Returns:
        List of processed strings in lowercase
    """
    results = []
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        await asyncio.sleep(0.1)
        processed = [item.lower() for item in batch]
        results.extend(processed)
    return results


async def parallel_fetch(urls: List[str]) -> List[Optional[Dict]]:
    """
    Fetch data from multiple URLs in parallel.
    
    Args:
        urls: List of URLs to fetch
    
    Returns:
        List of dictionaries or None for failed requests
    """
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return [r if not isinstance(r, BaseException) else None for r in results]


async def retry_operation(
    operation: Callable[[], Awaitable[Any]],
    max_retries: int = 3,
    delay: float = 1.0
) -> Any:
    """
    Retry an async operation with exponential backoff.
    
    Args:
        operation: Async callable to retry
        max_retries: Maximum number of retry attempts
        delay: Base delay between retries in seconds
    
    Returns:
        Result of the operation
    
    Raises:
        Exception: If all retry attempts fail
    """
    for attempt in range(max_retries):
        try:
            return await operation()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(delay * (attempt + 1))


async def stream_processor(
    data_stream: AsyncIterator[Any],
    callback: Callable[[Any], Awaitable[None]]
) -> int:
    """
    Process items from an async stream.
    
    Args:
        data_stream: Async iterator of items to process
        callback: Async function to call for each item
    
    Returns:
        Total number of items processed
    """
    count = 0
    async for item in data_stream:
        await callback(item)
        count += 1
    return count

# Made with Bob
