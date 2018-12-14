"""Simple examples of generators"""


def generate_even_values(limit):
    """Method that generates all even numbers from 0 up to limit
    The values are stored in a list"""
    values = []
    for value in range(0,limit+1,2):
        values.append(value)
    return values

def even_values_generator(limit):
    """Generator for all even numbers from 0 up to limit
    The values are generated one by one"""
    for value in range(0, limit + 1, 2):
        yield value



if __name__ == "__main__":
    # we get the list
    even_numbers = generate_even_values(10)
    for even_value in even_numbers:
        print("Even value: {}".format(even_value))

    print("Now using a generator ")
    for even_value in even_values_generator(10):
        print("Even value: {}".format(even_value))
