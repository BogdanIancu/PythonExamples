list1 = []
list1.append(50)
list1.append('Something')
list1.append(79)

for index,item in enumerate(list1):
    if type(item) == int and item > 55:
        print("Element {} is found at index {}".format(item, index))
    elif type(item) == int and item == 50:
        print("We found {} at index {}".format(item, index))
    else:
        print("Finally! {} at index {}".format(item, index))

i = 0
while i < len(list1):
    print("Element {} is found at index {}".format(list1[i],i))
    i+=1

ind = 0;
while True:
    ind+=1
    print("Iteration {}".format(ind))
    if ind >= len(list1):
        break;
