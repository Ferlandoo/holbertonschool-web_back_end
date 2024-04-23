#!/usr/bin/env python3
"""Tasks"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def measure_runtime() -> float:
    """Measures the runtime"""
    import time
    start = time.time()
    tasks = [task_wait_random() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
