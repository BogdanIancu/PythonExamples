import time
import asyncio
import random

start = time.time()


def get_time():
    return 'at %1.1f seconds' % (time.time() - start)


async def task1():
    # do something blocking
    print('task1 started work: {}'.format(get_time()))
    await asyncio.sleep(random.randint(1, 5))
    print('task1 ended work: {}'.format(get_time()))


async def task2():
    # do something blocking
    print('task2 started work: {}'.format(get_time()))
    await asyncio.sleep(random.randint(1, 5))
    print('task2 ended work: {}'.format(get_time()))


async def mainTask():
    print("Lets do some stuff, {}".format(get_time()))
    await asyncio.sleep(1)
    print("Done doing the main task!")


print("Starting the process !")

io_loop = asyncio.get_event_loop()
tasks = [
    io_loop.create_task(task1()),
    io_loop.create_task(task2()),
    io_loop.create_task(mainTask())
]

# tasks2 = [
#     asyncio.ensure_future(task1()),
#     asyncio.ensure_future(task2()),
#     asyncio.ensure_future(mainTask())
# ]
io_loop.run_until_complete(asyncio.wait(tasks))
io_loop.close()

print("The END")
