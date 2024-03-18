#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written and write
an async routine called wait_n that takes in 2 int arguments (in this order): 
n and max_delay. You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of the 
delays should be in ascending order without using sort() because of concurrency.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    # Use asyncio.gather() to concurrently execute wait_random n times

    delay = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(delay)

