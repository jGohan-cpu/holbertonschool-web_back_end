#!/usr/bin/env python3
"""Script that takes two integers args page and page_size"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return tuple of size two"""

    end: int = page * page_size
    start: int = end - page_size

    return (start, end)
