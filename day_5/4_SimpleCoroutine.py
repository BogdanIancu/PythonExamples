import asyncio


def something():
    print("Simple function !")
    # will not work
    # await do_something_coroutine()


async def do_something_coroutine():
    print("Simple coroutine !")

    # blocking operation
    result = await do_something_else_coroutine()

    print("Received value: " + str(result))
    print("First coroutine - The END")


async def do_something_else_coroutine():
    print("2nd coroutine !")
    return 10


something()

# running the coroutine
loop = asyncio.get_event_loop()

# does not work with normal functions
# TypeError: A Future, a coroutine or an awaitable is required
# loop.run_until_complete(something())

loop.run_until_complete(do_something_coroutine())

# loop = asyncio.get_event_loop()
# wrapping a coroutine in a task
task = [loop.create_task(do_something_else_coroutine())]
loop.run_until_complete(asyncio.wait(task))


loop.close()
