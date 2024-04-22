#!/usr/bin/env python3
"""Basic async syntax"""
import asyncio
import random
import time


async def measure_time(n: int, max_delay: int) -> float:
    """Wait for a random delay and return it"""
    start = time.time()
    elem_list = []
    for _ in range(n):
        delay = random.uniform(0, max_delay)
        await asyncio.sleep(delay)
        elem_list.append(delay)
    end = time.time()
    total_time = end - start
    return total_time / n
