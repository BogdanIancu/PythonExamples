import threading
import time

N = int(1e8)

def sum_sequential(start_index:int , N):
    sum = 0
    
    for i in range(start_index, int(N), 1):
        sum += i
    return sum


def performance_test(function, start_index, N):
    start = time.time()
    function(start_index, N)
    end = time.time()
    print('Elapsed time is {}'.format(end-start))


class myThread (threading.Thread):
   def __init__(self, iStart, iEnd):
      threading.Thread.__init__(self)
      self.result = 0
      self.iStart = iStart
      self.iEnd = iEnd

   def run(self):
       print('starting with {} and {}'.format(self.iStart, self.iEnd))
       self.result = sum_sequential(self.iStart, self.iEnd)

def sum_threads(start, N):
    threads = []
    noThreads = 4
    for i in range(4):
        thread = myThread(int(i*N/noThreads), int((i+1)*N/noThreads))
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()

performance_test(sum_sequential, 0, N)
print('starting multiple threads')
performance_test(sum_threads, 0, N)
