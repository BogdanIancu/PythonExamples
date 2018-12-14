"""Exemplify main functions of the asyncio library"""
import asyncio


async def print_message(message, when):
    """Simple function that prints a message"""
    await asyncio.sleep(when)
    print(message)


async def check_prime(number):
    """Some intensive processing function"""
    print("checking {} ".format(number))
    for value in range(2,int(number/2)):
        await asyncio.sleep(0)
        reminder = number % value
        if reminder == 0:
            print("{} is not prime because is divided by {}".format(number,value))
            return False
    print("{} is prime ".format(number))
    return True

if __name__ == "__main__":

    # get the main event loop
    loop = asyncio.get_event_loop()

    # enabling debugging
    loop.set_debug(True)

    # check_prime(4576457457657475754767777771)

    # loop.run_in_executor(None, check_prime, 4576457457657475754767777771)

    # creating tasks - they start executing

    task1 = loop.create_task(print_message("Starting program", 3))
    task2 = loop.create_task(print_message("Connecting to Web server", 1))
    task3 = loop.create_task(check_prime(4576457457657475754767777771))

    #  run forever
    #  loop.run_forever()

    #  will generate an error as we don't wait on task_1
    #  loop.run_until_complete(task_2)

    #  will run ok - but is not ok
    # loop.run_until_complete(task1)

    loop.run_until_complete(asyncio.gather(task1, task2, task3))

    loop.close()

    print("The end")