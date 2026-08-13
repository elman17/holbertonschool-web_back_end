#!/usr/bin/env python3
"""This module provides an asynchronous generator function 'async_generator'."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times, waits 1 second asynchronously, and yields random float."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
