def func1(salary):
    print(salary+300)

# storing reference to func1 in bonus
bonus = func1
bonus(3000)
bonus(5000)
bonus(1000)


def func2(value):
    print('Starting execution of func2')
    #defined inner function inside func2 function
    def innerFunc():
        print(value)
    innerFunc()
    print('Finished execution of func2')

func = func2
func(2000)
func('Something')
func('Something else')
func(5000)

def func3(operation):
    print('Executing important ops')
    operation()
    print('Finished important ops')

@func3
def add():
    print(5+7)

@func3
def remove():
    print(12-10)

""" ops = func3
ops(add)
ops(remove) """

def func4():
    print('Executing again')
    v = 5
    def func5():
        print(v)
    return func5

var = func4()
var()
var()

def func6(function):
    print('Starting...')
    function()
    def func7():
        function()
        print('Finished func7')
    func7()
    return func7

def tmpFunc():
    print('I am an important function')

tmp = func6(tmpFunc) 
tmp()
tmp()