#!/usr/bin/env python3
"""Module: Task 3 - Task Wait Random."""
import asyncio


# Importing wait_random function from the previous Python file
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task for wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio task for wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
