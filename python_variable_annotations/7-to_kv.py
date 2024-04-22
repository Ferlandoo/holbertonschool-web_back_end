#!/usr/bin/env python3
"""Type-annotated function to_kv"""
from typing import Union


def to_kv(k: str, v: Union[int | float]) -> Union[str, float]:
    """Returns a tuple with a string and a float"""
    return (k, v * v)
