#!/usr/bin/env python3
"""Module: Task 1 - Concurrent Coroutines.
"""
import asyncio
from typing import List


# Importing wait_random coroutine from previous Python file
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with specified max_delay,
    returning the list of all the delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random coroutine.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
