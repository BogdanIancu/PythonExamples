list1 = [] # created an empty list
list1.append('My first element')
list1.append('My second element')
list1.append('My third element')
list2 = [50, 60]
print(list1)
print(list1[1])
print(list1[0:2])
print(list1[:1])

list1[1] = 'Something else'
print(list1[1])

#list1.append(list2)
#print(list1)
list1.extend(list2)
print(list1)
print(list1 + list2)

tuple1 = ('SomeValue', 1)
# tuple1[0]=5 # tuple values are immutable
print(tuple1[0])
print(tuple1[1])


student = {}
student["name"] = "Gigel"
student["surname"] = "Popel"
student["group"] = "1075"
student["address"] = "Bd. Ion Mihalache Nr.15"

print(student) 