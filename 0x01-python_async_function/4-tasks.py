#!/usr/bin/env python3
"""Module: Task 4 - Task Wait N."""
import asyncio
from typing import List


# Importing task_wait_random function from the previous Python file
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times with specified max_delay,
    returning the list of all the delays in ascending order.

    Args:
        n (int): Number of times to execute task_wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    wait_times = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)]
    )
    return sorted(wait_times)
