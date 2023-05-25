import logging
import threading
import time
import concurrent.futures
include animate


'''
class FakeDatabase:
    def __init__(self):
        self.value = 0
    def update(self, name):
        logging.info("Thread %s : starting update", name)
        local_copy = self.value
        local_copy +=1
        time.sleep(0.1)
        self.value


def thread_funtion(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format= format, level = logging.INFO, datefmt = "%H:%M:%S")


    # now want to create multiple threads

    #threads = list()
    #for i in range(3):
    #    logging.info("Main : create and start thread %d. ", i )
     #   x = threading.Thread(target = thread_funtion, args = (i,))
      #  threads.append(x)
       # x.start()

    #for i, thread in enumerate(threads):
     #   logging.info("Main : before joining thread %d.", i)
      #  thread.join() # waits for the other threads to finish
       # logging.info("Main : thread %d done", i)
    #alternative method
    with concurrent.futures.ThreadPoolExecutor(max_workers = 3) as executor:
        executor.map(thread_funtion, range(3))'''


exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      print("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")
