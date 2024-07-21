import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Generator that parses input text and finds all numbers

    Yields:
        Numbers in provided text
    """
    pattern = r'\b\d+\.\d+\b'
    parsed_text = re.findall(pattern, text)
    for _ in parsed_text:
        yield float(_)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Function that uses number generator to calculate total profit

    Returns:
        Total profit
    """
    return sum(func(text))