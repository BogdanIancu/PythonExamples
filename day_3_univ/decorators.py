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