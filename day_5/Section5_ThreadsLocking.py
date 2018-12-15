import threading
from random import randint

class Wallet:
    def __init__(self, initialValue):
        self.balance = initialValue
    
    def pay(self, value):
        if(value <= self.balance):
            print('Paying {}'.format(value))
            self.balance -= value
            print('left: {}'.format(self.balance))
    def get_balance(self):
        return self.balance
    
class Client(threading.Thread):
    def __init__(self, wallet, name):
        threading.Thread.__init__(self)
        self.wallet = wallet
        self.name = name
    def run(self):
        while(self.wallet.get_balance() > 0):
            value = randint(0, 10)
            print('{} is trying to pay {}'.format(self.name, value))
            # Lock to synchronize threads
            threadLock.acquire()
            self.wallet.pay(value)
            # Free lock 
            threadLock.release()

# adding the lock
threadLock = threading.Lock()

wallet = Wallet(10000)
client1 = Client(wallet,'John')
client2 = Client(wallet,'Alice')

client1.start()
client2.start()

client1.join()
client2.join()

