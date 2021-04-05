import os
import threading
import time
import queue

exitFlag = 0
maystop=0
callback_queue = queue.Queue()

def printit (x):
    print ("X = %d"%x)

def deccount(x):
    global maystop
    maystop = maystop+x

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        callback_queue.put(printit(counter))
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
    callback_queue.put(deccount(2))


# Create new threads
thread1 = myThread(1, "Thread-1", 0.1)
thread2 = myThread(2, "Thread-2", 0.1)

# Start new Threads
thread1.start()
thread2.start()

while maystop < 4:
    #print ("maystop = %d"%maystop)
    try:
        callback = callback_queue.get(False)  # doesn't block
        if not callback  is None:
            callback()
        else:
            print ("None function")
    except queue.Empty:  # raised when queue is empty
        pass
    time.sleep(0.1)
print ("Exiting Main Thread")