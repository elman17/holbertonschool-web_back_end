#!/usr/bin/env python3
"""This module provides an asynchronous"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 100 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
