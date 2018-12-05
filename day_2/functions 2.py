from functools import reduce
# import functools
def simple_function():
    print('I am a simple function')

simple_function()

def simple_function_return():
    print('I am using a Pythonic approach')
    return

simple_function_return()

def function_params(x, y):
    print('Called function parameters: {} {}'.format(x,y))
    return

function_params(10,20)

def function_arguments(x, *argv):
    # argv[0] = 250 # read-only values
    print('{} is the mandatory paramenter. {} are the arguments values'.format(x, argv))
    return

function_arguments(200)
# function_arguments() # Error
function_arguments(200, 300) # error
def function_kwargs(x, **kwargs):
    print('{} mandatory parameter value.'.format(x))
    print('{} keyword arguments values.'.format(kwargs))
    return

function_kwargs(100)
function_kwargs(100,name='Gigel', surname='Popel')

def function_args_kwargs(x, *argv, **kwargs):
    print('{} mandatory value'.format(x))
    print('{} variable length args'.format(argv))
    print('{} keyword arguments'.format(kwargs))
    return

function_args_kwargs(20)
function_args_kwargs(10, 20, 30)
function_args_kwargs(10, 20, 30, name='Doe', surname='Joshn')

# print(globals())

values = []
values.append('MY First VALUE')
values.append('my SECOND vALue')
values.append('My THird VALUE')

def transform_lower(element):
    return element.lower()

formattedValues = map(transform_lower, values)
for item in formattedValues:
    print(item)

formattedValues = map(lambda x: x.lower(), values)
for item in formattedValues:
    print(item)


def greater_values(x):
    return x>20

greaterValues = filter(greater_values, range(25))
for item in greaterValues:
    print(item)

greaterValues = filter(lambda x: x > 20, range(25))
for index,item in enumerate(greaterValues):
    print('{} can be found at index: {}'.format(item, index))

salaries = [1500, 2000, 3000, 2500]
bonusSalaries = filter(lambda x: x>2500, map(lambda x: x+500, salaries))
for index, item in enumerate(bonusSalaries):
    print('Emplyee {} got a salary of: {} EUR'.format(index, item))

def get_total_salaries(prev, current):
    return prev + current

totalSalary = reduce(get_total_salaries, salaries)
print('Total salary of employees = {} EUR'.format(totalSalary))

avgSalary = reduce(lambda x,y: x+y, salaries)/len(salaries)
print('The average salary for an employee is: {}'.format(avgSalary))

# Map using list comprehension
formattedValue = [item.upper() for item in values]
for item in formattedValue:
    print(item)

filteredValues = [item for item in range(25) if item > 20]
for item in filteredValues:
    print(item)

bigBonuses = [item+500 for item in salaries if item > 2000]
for item in bigBonuses:
    print(item)

cities = {}
cities["Bucuresti"] = 20000
cities["Cluj"] = 25000
cities["Brasov"] = 23000
cities["Iasi"] = 15000
cities["Vaslui"] = 1000

ecoCities = {k:v for (k,v) in cities.items() if v>20000}
for (k, v) in ecoCities.items():
    print('Orasul {} aloca un buget de {} pentru spatiile verzi'.format(k, v))

print(ecoCities.items())

residual = 50

def valueASD():
    residual = 70
    def valueDSA():
        print(residual)
    valueDSA()
    return

valueASD()