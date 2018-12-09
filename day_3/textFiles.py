""" file = open('cities.txt', 'w')
file.write('Something\n')
file.write('Something else\n')
file.close() """

def file_writer(fileName, value):
    file = open(fileName, 'a')
    file.write('{}\n'.format(value))
    file.close()

def file_reader(fileName):
    fileValues = []
    file = open(fileName, 'r')
    for line in file:
        values = line.strip().split(",")
        student = {}
        student["name"] = values[0]
        student["surname"] = values[1]
        student["age"] = values[2]
        student["address"] = values[3]
        fileValues.append(student)
    file.close()
    return fileValues

""" file_writer('cities.txt', 'Brasov')
file_writer('cities.txt', 'Sibiu')
file_writer('cities.txt', 'Constanta')
file_writer('cities.txt', 'Comarnic')
file_writer('cities.txt', 'Pitesti')
file_writer('cities.txt', 'Bucuresti') """

""" for city in file_reader('cities.txt'):
    print(city) """

#file_writer('dummy.txt', 'residual value')

file_writer('students.txt','Gigescu,Popel,25,Calea Dorobanti')
file_writer('students.txt', 'Popescu,Gigel,27,Calea Ferentari')
file_writer('students.txt', 'Ana,Mere,24,Bd. Regina Elisabeta')
file_writer('students.txt', 'Maria,Pere,26,Drumul Taberei')

for student in file_reader('students.txt'):
    for (k,v) in student.items():
        print('{}: {}'.format(k, v))

def smart_file_writer(fileName, value):
    with open(fileName, 'a') as file:
        file.write('{}\n'.format(value))

def smart_file_reader(fileName):
    with open(fileName, 'r') as file:
        for line in file:
            print(line.strip())

smart_file_writer('test.txt', 'value1')
smart_file_writer('test.txt', 'value2')
smart_file_writer('test.txt', 'value3')
smart_file_reader('test.txt')
