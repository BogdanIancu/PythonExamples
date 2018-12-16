import time
import threading

class myThread(threading.Thread):
  def __init__(self, id, nr_afisari):
    threading.Thread.__init__(self)
    self.id = id
    self.nr_afisari = nr_afisari
  def run(self):
    print_hello(self.id, self.nr_afisari)

def print_hello(id, nr_afisari):
  for i in range(nr_afisari):
    print("Hello de la {}".format(id))
    time.sleep(2)


#varianta secventiala
print_hello(1,2)
print_hello(2,3)

#varianta multithreading
print("**************************")
#t1 = threading.Thread(group=None,target=print_hello,name='T1',args=(1,2))
#t2 = threading.Thread(group=None,target=print_hello,name='T1',args=(2,3))

t1 = myThread(1,2)
t2 = myThread(2,3)

t1.start()
t2.start()

t1.join()
t2.join()

print("The END")
