def func1():
    var = 5
    def func2():
        print(var)
    return func2

tmp = func1()
tmp()

def iterator_func():
    values = []
    for x in range(0, 3):
        def dummy(x=x):
            print(x)
        values.append(dummy)
    return values


dummies = iterator_func()
dummies[0]()
dummies[1]()
dummies[2]()

def employee_factory(employeeType):
    if employeeType=='CEO':
        def ceo(name, surname):
            print('{} {} is a great {}. {} ROCKS!'.format(name, surname, employeeType, surname))
        return ceo
    elif employeeType=='INTERN':
        def intern(name, surname):
            print('{} {} is doing a great job. {} will get a BONUS!'.format(name, surname, surname))
        return intern
    else:
        def employee(name, surname):
            print('{} {} is just an employee. {} is doing good.'.format(name, surname, surname))
        return employee

ceo = employee_factory('CEO')
intern = employee_factory('INTERN')
employee = employee_factory('EMPLOYEE')

ceo('GIGESCU', 'POPEL')
intern('POPESCU', 'GIGEL')
employee('ANA', 'PERE')