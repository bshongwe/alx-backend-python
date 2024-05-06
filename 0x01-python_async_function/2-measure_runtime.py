#!/usr/bin/env python3
"""Module: Task 2 - Measure Runtime."""
import asyncio
import time

# Importing wait_n function from the previous Python file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Computes the average runtime of wait_n.

    Args:
        n (int): Number of iterations.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average runtime per iteration.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
