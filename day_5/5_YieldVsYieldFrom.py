"""exemplify the difference between yield and yield from"""

# use case 1 - getting data from a generator
def counter():
    """A generator that behaves like a counter"""
    for value in range(5):
        yield "<{}>".format(value)

def counter_wrapper(generator):
    """version 1 - using a manual iterator and yield"""
    for value in generator:
        yield value

def counter_wrapper_2(generator):
    """version 2 - using yield from"""
    yield from generator


def use_case_1():
    """use case: Reading data from a generator using yield from"""
    # wrapper = counter_wrapper(counter())
    wrapper = counter_wrapper_2(counter())
    for value in wrapper:
        print(value)

# use case 2 - sending data to a generator (coroutine)

def value_writer():
    """A coroutine that writes data *sent* to it to an output source"""
    while True:
        value = (yield)
        print(">>>> ", value)


def writer_wrapper(coroutine):
    coroutine.send(None)
    while True:
        try:
            received_value = (yield)
            coroutine.send(received_value)
        except StopIteration:
            pass


def writer_wrapper_2(coroutine):
    """the same as writer_wrapper but with yield from"""
    yield from coroutine


def use_case_2():
    writer = value_writer()
    # wrapper = writer_wrapper(writer)
    wrapper = writer_wrapper_2(writer)
    wrapper.send(None)  # init the coroutine
    for i in range(5):
        wrapper.send(i)

#
# use case 3 - managing exceptions with yield from
#

class SpamException(Exception):
    """A custom exception class"""
    pass

def value_writer_2():
    """A coroutine that writes data *sent* to it to an output source. It also checks for SpamExceptions"""
    while True:
        try:
            value = (yield)
        except SpamException:
            print('### Error ###')
        else:
            print(">>>> ", value)

def writer_wrapper_3(coroutine):
    """Manually catches exceptions and throws them"""
    coroutine.send(None)  # prime the coro
    while True:
        try:
            try:
                x = (yield)
            except SpamException as e:   # This catches the SpamException
                coroutine.throw(e)
            else:
                coroutine.send(x)
        except StopIteration:
            pass

def use_case_3():
    writer = value_writer_2()
    # it will not work as writer_wrapper can't manage exceptions
    # wrapper = writer_wrapper(writer)

    # this works
    # wrapper = writer_wrapper_3(writer)
    # and also this
    wrapper = writer_wrapper_2(writer)

    wrapper.send(None)
    for i in range(5):
        if i == 2:
            wrapper.throw(SpamException)
        else:
            wrapper.send(i)





# test use case 1
# use_case_1()

# test use case 2
# use_case_2()

use_case_3()
