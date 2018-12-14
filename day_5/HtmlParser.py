import time
import urllib.request
import asyncio
import aiohttp
import concurrent.futures

URL = 'https://api.github.com/events'
MAX_CLIENTS = 3


def get_data_sync(pid):
    print("Fetch sync process {} started".format(pid))
    start = time.time()
    response = urllib.request.urlopen(URL)
    datetime = response.getheader('Date')

    print("Process {}: {}, took: {:.2f} seconds".format(
        pid, datetime, time.time() - start))

    return datetime


async def get_data_async(pid):
    print("Fetch async process {} started".format(pid))
    start = time.time()
    async with aiohttp.request('GET', URL) as response:
      #response = yield from aiohttp.request('GET', URL)
      datetime = response.headers.get('Date')
      

    print("Process {}: {}, took: {:.2f} seconds".format(
        pid, datetime, time.time() - start))

    response.close()

    return datetime


def synchronous():
    start = time.time()
    for i in range(1, MAX_CLIENTS + 1):
        get_data_sync(i)
    print("Process took: {:.2f} seconds".format(time.time() - start))


async def asynchronous():
    start = time.time()
    tasks = [asyncio.ensure_future(
        get_data_async(i)) for i in range(1, MAX_CLIENTS + 1)]
    await asyncio.wait(tasks, return_when=concurrent.futures.ALL_COMPLETED)
    print("Process took: {:.2f} seconds".format(time.time() - start))


# print("Synchronous:")
# synchronous()

print("Asynchronous:")
loop = asyncio.get_event_loop()
loop.run_until_complete(asynchronous())
loop.close()
