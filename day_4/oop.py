import copy

class Student:
    #__slots__ = '__id', 'nume', 'varsta', '__dict__'
    numeUniversitate = 'unibuc'
    def __init__(self, nume='Anonim', varsta=18):
        self.__id = 1
        self.nume = nume
        self.varsta = varsta

    def __del__(self):
        print('S-a apelat destructorul pt ' + self.nume)

    @property
    def id(self):
        return self.__id + 100

    @id.setter
    def id(self, value):
        self.__id = value

    def afisare(self):
        print('Nume: ' + self.nume)
        print('Varsta: ' + str(self.varsta))

    @staticmethod
    def afisareNumeUniversitate():
        print(Student.numeUniversitate)

class StudentBursier(Student):
    def __init__(self, nume, varsta, valoareBursa):
        Student.__init__(self, nume, varsta)
        self.valoareBursa = valoareBursa

class Grupa:
    def __init__(self):
        self.studenti = []

    def add(self, student):
        self.studenti.append(student)

    def afisare(self):
        print("Studenti:")
        for s in self.studenti:
            s.afisare()

    def clone(self):
        clona = Grupa()
        clona.studenti = self.studenti[:]
        return clona

    def __add__(self, grupa2):
        rezultat = Grupa()
        for s in self.studenti:
            rezultat.add(s)
        for s in grupa2.studenti:
            rezultat.add(s)
        return rezultat

student1 = Student('Gigel', 20)
Student.adresaFacultate = 'Piata Universitatii'
#student1.medie = 10
print(student1.nume)
print(student1.varsta)
print(Student.numeUniversitate)
print(Student.adresaFacultate)
print(student1.numeUniversitate)
print(student1.id)
#print(student1.medie)
print(student1.__dict__)
print(student1._Student__id)
student2 = Student()
print(student2.nume)
#print(student2.medie)
student1.afisare()
grupa = Grupa()
grupa.add(student1)
grupa.add(student2)
grupa.afisare()
Student.afisareNumeUniversitate()
student1.id = 5
print(student1.id)
student3 = student2
student3.nume = 'John'
print(student2.nume)
student4 = copy.deepcopy(student2)
student4.nume = 'George'
print(student2.nume)
print(student4.nume)
grupa2 = grupa.clone()
grupa2.add(student4)
grupa.afisare()
grupa3 = grupa + grupa2
print("------------")
grupa3.afisare()
student5 = StudentBursier('Vasile', 27, 900)
