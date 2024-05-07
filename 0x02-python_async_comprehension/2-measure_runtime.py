#!/usr/bin/env python3
"""
Module: Task 2: Run time for four parallel comprehensions.
"""
import asyncio
import time
from importlib import import_module as using


# Import the async_comprehension function from the
# '1-async_comprehension' module
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times and measures the total
    execution time.

    This function measures the total execution time of
    async_comprehension by executing it asynchronously
    4 times using asyncio.gather. It starts measuring
    time before execution and stops after all
    executions are completed.

    Returns:
        float: The total execution time in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
