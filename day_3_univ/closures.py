def func1():
    var = 5
    def func2():
        print(var)
    return func2

tmp = func1()
tmp()