"""Sample file for testing --write-docs feature."""


def calculate_sum(a, b):
    return a + b


def process_data(items, threshold=0.5):
    results = []
    for item in items:
        if item > threshold:
            results.append(item * 2)
    return results


class DataProcessor:
    
    def __init__(self, name):
        self.name = name
        self.data = []
    
    def add_item(self, item):
        self.data.append(item)
    
    def get_total(self):
        return sum(self.data)


async def fetch_data(url, timeout=30):
    import asyncio
    await asyncio.sleep(1)
    return {"status": "ok", "url": url}

# Made with Bob
