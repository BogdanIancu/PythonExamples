import asyncio
import random

async def coroutine(label):
    print(">>", label)
    await asyncio.sleep(random.uniform(1, 3))
    print("<<", label)
    return label


def group_test():
    """executing all tasks together using group"""
    loop = asyncio.get_event_loop()

    group1 = asyncio.gather(*[coroutine("group 1.{}".format(i)) for i in range(1, 3)])
    group2 = asyncio.gather(*[coroutine("group 2.{}".format(i)) for i in range(1, 5)])

    all_groups = asyncio.gather(group1, group2)

    results = loop.run_until_complete(all_groups)

    loop.close()

    print(results)

def wait_test():
    """executing tasks in phases using wait"""
    loop = asyncio.get_event_loop()

    tasks = [coroutine(i) for i in range(1, 11)]

    print("Get first result:")
    finished, unfinished = loop.run_until_complete(
        asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED))

    for task in finished:
        print(task.result())
    print("unfinished:", len(unfinished))

    print("Get more results in 2 seconds:")
    finished2, unfinished2 = loop.run_until_complete(
        asyncio.wait(unfinished, timeout=2))

    for task in finished2:
        print(task.result())
    print("unfinished2:", len(unfinished2))

    if unfinished2:
        print("Get all other results:")
        finished3, unfinished3 = loop.run_until_complete(asyncio.wait(unfinished2))

        for task in finished3:
            print(task.result())

    loop.close()


# test group function
# group_test()

# test wait functions
wait_test()