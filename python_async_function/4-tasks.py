#!/usr/bin/env python3
"""Tasks"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of delays"""
    elem_list = []
    for _ in range(n):
        elem_list.append(await task_wait_random(max_delay))
    return sorted(elem_list)
