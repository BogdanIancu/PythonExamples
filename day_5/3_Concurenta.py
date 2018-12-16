import threading
from random import randint

class PortofelElectronic:
  def __init__(self, suma_initiala):
    self.suma = suma_initiala
  
  def plata(self, valoare):
    if(valoare <= self.suma):
      print("Platesc {}".format(valoare))
      self.suma -= valoare
  
  def get_suma(self):
    return self.suma
  
class Client(threading.Thread):
  def __init__(self, nume, portofel):
    threading.Thread.__init__(self)
    self.portofel = portofel
    self.nume = nume
  def run(self):
    while (self.portofel.get_suma()>0):
      suma_de_plata = randint(0, 10)
      print("{} incearca sa plateasca {}".format(self.nume, suma_de_plata))
      lock_plata.acquire()
      self.portofel.plata(suma_de_plata)
      lock_plata.release()
      print('In portofel mai sunt {}'.format(self.portofel.get_suma()))

#definire lock pentru a bloca accesul concurent la plata
lock_plata = threading.Lock()

portofel = PortofelElectronic(10000)
client1 = Client("Gigel",portofel)
client2 = Client("Ana",portofel)

client1.start()
client2.start()

client1.join()
client2.join()

print("Sfarsit")