#!/usr/bin/env python3
"""Script takes a float and returns a float"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return float"""
    return sum(mxd_list)
