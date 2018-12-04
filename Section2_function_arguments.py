import sys

def main():
     print("hello world!")
     return



def test_var_args(value, *argv):
    print("first argument:", value)
    for arg in argv:
        print("another argument through *argv:", arg)
    return


def test_var_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
    return

if __name__ == "__main__":
    main()

test_var_args('Sunday', 'python', 'training', 'test')
test_var_kwargs(trainer="John", day = "Sunday", location = "Cegeka")

print(sys.argv)