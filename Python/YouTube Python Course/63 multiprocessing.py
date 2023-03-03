"""
Multiprocessing = running tasks in parallel on different CPU cores. Bypasses GIL used for threading. 
Multiprocessing is better for CPU bound tasks (heavy CPU usage)
Multithreading is better for I/O bound tasks (waiting around)
"""

from multiprocessing import Process, cpu_count
import time

#Create a single process that counts to 1 billion
"""
def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter, args=(1000000000,))
    a.start()
    a.join()

    print("Finished in:", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()
"""

#Now create 2 processes that each count to 500 million
def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))
    
    a.start()
    b.start()

    a.join()
    b.join()

    print("Finished in:", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()

