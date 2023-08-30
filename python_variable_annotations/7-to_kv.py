#!/usr/bin/env python3
"""Script takes string or floats and return annotate floats"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple"""
    return tuple([k, v*v])
