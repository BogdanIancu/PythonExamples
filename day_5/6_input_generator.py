

def functie_care_asteapta_input():
    print('start functie')
    valoare = (yield)
    print('Am primit valoare {}'.format(valoare))


generator = functie_care_asteapta_input()
print('start generator')
generator.send(None)
print('Generator blocat ! Asteapta valoare')
#generator.send(10)

for i in generator:
    generator.send(10)

