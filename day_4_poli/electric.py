from vehicle import Vehicle

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, chassis, year, price, batteryPower):
        #Vehicle.__init__(self,make, model, chassis, year, price)
        super(ElectricVehicle, self).__init__(make, model, chassis, year, price)
        self.batteryPower = batteryPower
    
    def __str__(self):
        return '{}\nBattery Capacity: {} mAh'.format(Vehicle.__str__(self), self.batteryPower)


ecar = ElectricVehicle("Tesla", "Model X", "W2313131313131", 2017, 120000, 50000)
ecar1 = ElectricVehicle("BMW", "i8", "W2813718371893271", 2016, 120000, 40000)
ecar2 = ElectricVehicle("Rimac", "f1", "W78687678678687", 2018, 200000, 100000)

print(ecar)
print(ecar1)
print(ecar2)