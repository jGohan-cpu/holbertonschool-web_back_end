#!/usr/bin/env python3
"""Script coroutine run parallel with asyncio.gather"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that run in parallel"""

    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    total_time = time.perf_counter() - start

    return total_time
