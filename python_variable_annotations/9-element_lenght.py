#!/usr/bin/env python3
""""Script return values of appropiate type"""

from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list"""
    return [(i, len(i)) for i in lst]
