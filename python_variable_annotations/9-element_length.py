#!/usr/bin/env python3
"""Type-annotated function element_length"""
from typing import Sequence, Tuple, List


def element_length(lst: Sequence[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples"""
    return [(i, len(i)) for i in lst]
