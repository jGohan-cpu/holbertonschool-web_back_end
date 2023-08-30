#!/usr/bin/env python3
"""Script takes a float and return multiplier of floats"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates function"""
    def multiplier_function(d: float) -> float:
        """Returns multplier result"""
        return d * multiplier
    return multiplier_function