#!/usr/bin/env python3
"""Basic async syntax"""
import asyncio
import random


async def measure_time(n: int, max_delay: int) -> float:
    """Wait for a random delay and return it"""
    start = asyncio.get_event_loop().time()
    elem_list = []
    for _ in range(n):
        delay = random.uniform(0, max_delay)
        await asyncio.sleep(delay)
        elem_list.append(delay)
    end = asyncio.get_event_loop().time()
    total_time = end - start
    return total_time / n
