#!/usr/bin/env python3
"""
Module: Task 1 - Asynchronous Comprehension.
"""
from typing import List
from importlib import import_module as using


# Import the async_generator function from the '0-async_generator' module
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously generates a list of 10 random numbers.

    Utilizes async_generator to asynchronously generate a sequence
    of 10 random floating-point numbers. The list comprehension
    asynchronously iterates over the generated numbers and constructs
    a list containing them.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [num async for num in async_generator()]
