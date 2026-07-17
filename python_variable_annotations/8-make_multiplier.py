#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function"""

    def multiplier_function(n: float) -> float:
        return n * multiplier

    return multiplier_function
