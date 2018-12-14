import random
from time import sleep
import asyncio


def task(pid):
    """Synchronous task"""
    sleep(random.randint(0, 2) * 0.001)
    print("Task {} is done".format(pid))


async def task_async(pid):
    """Coroutine task"""
    await asyncio.sleep(random.randint(0, 2) * 0.001)
    print("Task {} is done".format(pid))


def synchronous():
    for i in range(1, 10):
        task(i)


async def asynchronous():
    # tasks = [asyncio.ensure_future(task_async(i)) for i in range(1, 10)]
    # yield from asyncio.wait(tasks)


    # using blocking ops is the same syncronous problem
    for i in range(1,10):
        await task_async(i)


print('Synchronous:')
synchronous()

io_loop = asyncio.get_event_loop()
print('Asynchronous:')
io_loop.run_until_complete(asynchronous())
io_loop.close()
