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

""" def add(x,y):
    return 'Suma elementelor {} si {} este: {}'.format(x,y,x + y)

def substract(x,y):
    print('Diferenta dintre {} si {} este: {}'.format(x,y,x-y))

sum = add # stored reference of function add to variable sum
print(sum(5,9))
print(sum(10,19))
print(sum(15,20))
dif = substract # stored reference of function substract to variable dif
dif(10,7)
dif(5,2)
dif(15,12) """

""" def dummyFunc():
    functions = []
    for i in range(0,3):
        print('Added Element: {}'.format(i))
        def random():
            print('Some important operation')
        functions.append(random)
    return functions

values = dummyFunc()
values[0]()
values[1]()
values[2]() """

""" def func1():
    print('Started execution of func1')
    def func2():
        print('I am an inner function')
    func2()
    func2()
    print('Finished execution of func1')

inner = func1
inner() """

""" def operations(func):
    print('Started execution of {}'.format(func.__name__))
    func()
    print('Finished execution of {}'.format(func.__name__))

def add():
    print('Suma dintre {} si {} este: {}'.format(5,7,5+7))

def substract():
    print('Diferenta dintre {} si {} este: {}'.format(12,5,12-5))

def multiply():
    print('Produsul dintre {} si {} este: {}'.format(2,3,2*3))

def divide():
    print('Catul impartirii dintre {} si {} este: {}'.format(10, 5, 10/5))

ops = operations
ops(add)
ops(substract)
ops(multiply)
ops(divide) """

def combinator(function):
    print('Started execution of combinator function')
    def innerCombinator():
        print('Started execution of innerCombinator function')
        print('Started execution of {}'.format(function.__name__))
        function()
        print('Finished exeuction of {}'.format(function.__name__))
        print('Finished execution of innerCombinator function')
    
    function()
    innerCombinator()
    print('Finished execution of combinator function')
    return innerCombinator

def important_op():
    print('Some important operation')

innerComb = combinator(important_op)
innerComb()
innerComb()