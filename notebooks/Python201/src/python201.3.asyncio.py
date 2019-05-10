import time
import asyncio
import aiohttp
import requests


URL = 'https://www.uol.com.br'  # 'https://google.com.br'


async def aio_heavy(i, session):
    async with session.get(URL) as resp:
        if resp.status == 200:
            content = await resp.text()
            return True, i
        return False, i


async def asyncio_example(NUMBERS):
    items = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in NUMBERS:
            tasks.append(aio_heavy(i, session))
        items = await asyncio.gather(*tasks)
    return items


def io_heavy(i):
    r = requests.get(URL)
    if r.status_code == 200:
        content = r.text
        return True, i
    return False, i


def regular_example(NUMBERS):
    items = []
    for i in NUMBERS:
        items.append(io_heavy(i))
    return items


NUMBERS = range(0, 20)

start = time.time()
print(asyncio.run(asyncio_example(NUMBERS)))  # Python 3.7+
print(f'AsyncIO took: {round(time.time() - start, 2)} seconds')

start = time.time()
print(regular_example(NUMBERS))
print(f'Regular took: {round(time.time() - start, 2)} seconds')