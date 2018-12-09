import functools
def monitor(function):
    def wrapper():
        print('Starting monitoring {}'.format(function.__name__))
        function()
        print('Stopped monitoring {}'.format(function.__name__))
    
    return wrapper


@monitor
def add_todo():
    print('ADD_TODO_REQUEST COMPLETED')

add_todo()

def request_monitor(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print('Started request function: {}'.format(function.__name__))
        function(*args, **kwargs)
        print('Finished request function: {}'.format(function.__name__))
    return wrapper

@request_monitor
def add_to_do(todo):
    print('ADD_TODO_REQUEST STATUS: PENDING')
    print('ADD_TODO_REQUEST STATUS: COMPLETED {}'.format(todo))

todo = {}
todo['taskName'] = 'Training Python'
todo['priority'] = 'Medium'
todo['duration'] = 6

add_to_do(todo)
print(add_to_do.__name__)

""" 
simple_decorator is a function that takes one argument of type callable
when we decorate any function with @simple_decorator the function will be
called automatically with two more instructions to monitor the begining and 
ending of the execution
"""
"""
def simple_decorator(func):
    print('{} started to execute'.format(func.__name__))
    func()
    print('{} finished to execute'.format(func.__name__))


@simple_decorator
def add():
    print('Suma dintre {} si {} este: {}'.format(10,20,10+20))

@simple_decorator
def substract():
    print('Diferenta dintre {} si {} este: {}'.format(15,5,15-5))

# add() - cannot call anymore because of the decoration
# substract() - cannot call anymore because of the decoration
 """

""" def monitor(function):
    def wrapper():
        print('Started execution of {}'.format(function.__name__))
        function()
        print('Finished execution of {}'.format(function.__name__))
    return wrapper()

@monitor
def add():
    print('Suma de {} si {} este: {}'.format(50, 40, 50+40))

@monitor
def substract():
    print('Diferenta dintre {} si {} este: {}'.format(50,40,50-40)) """

""" def spider_bite(subject):
    def wrapper():
        print('Radioactive Spider coming near {}'.format(subject.__name__))
        person = subject()
        person['skills'].append('Jumping from buildings')
        person['skills'].append('Climbing walls')
        person['skills'].append('Throwing spider web')
        person['alias'] = 'Spider Man'
        print('{} is mutated'.format(subject.__name__))
        return person
    return wrapper

@spider_bite
def peter_parker():
    person = {}
    person['name'] = 'Peter Parker'
    person['skills'] = ['Math', "Fizica", "English", "Cooking"]
    return person

print(peter_parker()['alias'])
for skill in peter_parker()['skills']:
    print(skill)

 """

def mutation_factory(human):
    def wrapper(*args, **kwargs):
        print('Trying to apply mutation to {}'.format(human.__name__))
        newObject = human(*args, **kwargs)
        mutation = args[0]
        newObject['skills'].extend(mutation['skills'])
        newObject['alias'] = '{} {}'.format(mutation['animal'], newObject['name'].split(" ")[0])
        print('Mutation to {} completed'.format(human.__name__))
        return newObject
    return wrapper    

@mutation_factory
def john_doe(mutation):
    person = {}
    person['name'] = 'JOHN DOE'
    person['skills'] = ['Cooking', 'Singing']
    return person

mutation = {}
mutation['animal'] = 'Lion'
mutation['skills'] = ['Huge Strength', 'Claws', 'Deadly Bite']

print(john_doe(mutation))


    