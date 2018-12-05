vb = "I am a double quoted string"
vb1 = 'I am a single quoted string'
print(vb)
print(vb1)
vb2 = vb.upper()
print(vb2)
print(vb[2]) #prints second character from string vb
print(vb[2:4]) #prints characters from index 2 to index 4(not included)
print(vb[:7]) #prints characters from start of the string to index 7(not included)
print(vb[5:]) #prints chracters from index 5(included) to the end of the string
print(vb[:]) #prints entire string

print(vb.replace('a', 'z'))
print(vb.split())
print(vb[2:5].upper())
print(vb.find('q'))

vb3 = 15
vb4 = 'John'

print("Hello {}! Wow you are so young: just {} years old.".format(vb4, vb3))
print("""
    I am
    a 
    multiline
    message""")
print("Hello %s! Wow you are so young: just %i years old." % (vb4, vb3))
vb5 = 'dog'
vb6 = "dog"
print(vb5==vb6)