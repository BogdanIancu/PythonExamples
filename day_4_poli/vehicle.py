class Vehicle(object):
    def __init__(self, make, model, chassis, year, price):
        self.make = make
        self.model = model
        self.chassis = chassis
        self.year = year
        self.price = price

    def __str__(self):
        return 'Autovehiculul: {}\nModel: {}\nSeria de sasiu: {}\nAnul de fabricatie: {}\nPret: {}'.format(self.make, self.model, self.chassis, self.year, self.price)

if __name__ == "__main__":
    auto1 = Vehicle("Audi", "A5", "W2178361673521", 2015, 15000)
    auto2 = Vehicle("Mazda", "3", "W2371631863131", 2017, 20000)
    auto3 = Vehicle("BMW", "M6", "W3768268724622", 2018, 100000)

    print(auto1)
    print(auto2)
    print(auto3)

