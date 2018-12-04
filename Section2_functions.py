def request_string():
    input_value = input("Insert a word:")
    print("Thank you for "+input_value)
    return

def repeat_words(word,number):
    return (word + " ")*number

def sum(list):
    result = 0
    for value in list:
        result += value
    return result

def change_value(value):
    value = 100
    return
    
def change_global_value():
    value = 100
    return

def difference(value1, value2):
    return value1 - value2

def change_values( list ):
   for value in list:
       value = 10
   return

def change_values_2( list ):
   for i in range(0,len(list)):
       list[i] = 10
   return

def change_list( list ):
    list = [10,20,30]
    return


#request_string()
print(repeat_words("test",3))
print(repeat_words("something",1))
print(sum([1,2,3,4,5]))

#init value
value = 5

change_value(value)
print(value)


change_global_value()
print(value)

print("Difference: "+str(difference(2,1)))
print("Difference: "+str(difference(value2 = 1,value1 = 2)))

list = [1,2,3]
print(list)
change_values(list)
print(list)
change_values_2(list)
print(list)
change_list(list)
print(list)
