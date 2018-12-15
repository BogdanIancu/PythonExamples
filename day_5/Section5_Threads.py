import threading
import time

def thread_function_complex():
    for i in range(3):
        print("Hello World from thread {}!".format(threading.get_ident()))

def thread_function():
    print("Hello World !")

class myThread (threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)

   def run(self):
       time.sleep(2)
       print("Hello World 2!")

def main():
   #start a thread
   t1 = threading.Thread(group=None, \
   target=thread_function)
   t1.start()

   t2 = myThread()
   t2.start()

   #join the thread with main
   t1.join()




main()