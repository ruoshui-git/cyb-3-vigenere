from typing import Generator, List, TypeVar

T = TypeVar("T")

def chunks(lst: List[T], n: int):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
