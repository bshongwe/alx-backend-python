#!/usr/bin/env python3
"""Module: Task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds (exclusive on the upper
    bound) and eventually returns it.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: Random delay between 0 and max_delay seconds
        (exclusive on the upper bound).
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
