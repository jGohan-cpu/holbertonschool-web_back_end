#!/usr/bin/env python3
"""Script that random awaits and eventually
returns the value"""

import asyncio
import random


@asyncio.coroutine
async def wait_random(max_delay: int = 10) -> float:
    """Return delay value"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
