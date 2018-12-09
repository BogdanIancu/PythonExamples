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