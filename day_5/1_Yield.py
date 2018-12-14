"""Simple example to understand yield"""


def get_simple_message():
    """simple function that returns a string message"""
    return "Hello "

    # unreachable code
    # return "World "


def get_message():
    """simple function that returns mutiple strings - a generator"""
    print("Starting generating messages")
    yield "Hello "
    yield "World "
    yield "!"

if __name__ == "__main__":

    # prints the generator description
    print(get_message())

    # prints the generator description
    print(get_message())

    #getting the generator
    message_gen = get_message()

    #getting generated values
    print("Printing messages")
    print(next(message_gen))
    # print(message_gen.__next__())
    print(message_gen.__next__())
    print(message_gen.__next__())

    # getting a StopIteration exception
    # print(message_gen.__next__())

    for msg in get_message():
        print(msg)
