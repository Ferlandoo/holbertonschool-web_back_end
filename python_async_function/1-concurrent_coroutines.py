#!/usr/bin/env python3
"""Basic async syntax"""
from typing import List
import asyncio
import random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for a random delay and return it"""
    elem_list = []
    for _ in range(n):
        delay = random.uniform(0, max_delay)
        await asyncio.sleep(delay)
        elem_list.append(delay)
    return sorted(elem_list)
