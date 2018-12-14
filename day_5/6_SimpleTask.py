import asyncio

async def msg(text):
    await asyncio.sleep(0.1)
    print(text)


async def long_operation():
    print('long_operation started')
    await asyncio.sleep(3)
    print('long_operation finished')


async def main():
    await msg('first')

    # Now you want to start long_operation, but you don't want to wait it to finish:
    # long_operation should be started, but second msg should be printed immediately.
    # Create a task for the long operation:
    task = asyncio.ensure_future(long_operation())

    # blocking operation version
    # yield from long_operation()

    await msg('second')

    # await task to finish:
    await task


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
