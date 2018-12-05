from functools import reduce
#simple function    
def simple_function():
    print('I am a simple function')

simple_function()

# simple function with parameters
def function_params(x, y):
    print('Called function parameters with values: {}, {}'.format(x,y))

function_params(5,7)

# function with arguments

def function_arguments(x,*args):
    print('{} is the first parameter. Args contains: {}'.format(x, args))

function_arguments(6)
function_arguments(6,6,7,8,9)

# function with kwargs

def function_kwargumetns(x, **kwargs):
    print('{} is the mandatory parameter. Kwargs contains: {}'.format(x, kwargs))

function_kwargumetns(10)
function_kwargumetns(10, ceva = 10)
function_kwargumetns(10, ceva = 10, altceva = 20)

# function with args and kwargs
def function_args_kwargs(x, *args, **kwargs):
    print('{} is the mandatory prameter. Args contains: {}. Kwargs contains: {}'.format(x,args,kwargs))

function_args_kwargs(5)
function_args_kwargs(5,6)
function_args_kwargs(5,6,ceva=7)

# map example
def transform_lower(element):
    return element.lower()

values = []
values.append('MY First Value')
values.append('MY Second VALUE')
values.append('MY THIRD value')

for item in map(transform_lower, values):
    print(item)

#filter example
def get_big_values(element):
    return element > 20

values1 = range(25)

for item in filter(get_big_values, values1):
    print(item)

# reduce example

def get_total_salary(prev, current):
    return prev + current

salaries = [2500, 3000, 2000, 1500]

totalSalary = reduce(get_total_salary, salaries)
print(totalSalary)


# simple lambda expression 
simpleLambda = lambda x,y: x+y
print(simpleLambda(7,21))

#lambda function with map

for item in map(lambda x: x.upper(), values):
    print(item)

#lambda function with filter

for item in filter(lambda x: x > 20, range(25)):
    print(item)

#lambda function with reduce
avgSalary = reduce(lambda x,y: x+y, range(1,5))/4
print(avgSalary)

#lambda function for combining lists
values3 = [1,2,3,4]
values4 = [10,20,30]

for item in map(lambda x,y: x+y, values3, values4):
    print(item)

# list comprehension filter
filteredValues = [x for x in range(25) if x > 20]
for item in filteredValues:
    print(item)

#list comprehension mapping
mappedValues = [x*2 for x in range(5)]
for item in mappedValues:
    print(item)

#list comprehension mapping and filtering
combinedValues = [x*2 for x in range(25) if x > 20]
for item in combinedValues:
    print(item)


#dictionary comprehension filter
dic1 = {}
dic1["salary"]=20
dic1["age"]=40
dic2 = {k:v for (k,v) in dic1.items() if v > 20 }
print(dic2)

def valueASD():
    value = 'something'
    def valueDSA():
        print(value)
    valueDSA()
    return

valueASD()