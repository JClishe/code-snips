"""
A thread is a flow of execution, like a seperation of instructions. Each thread takes a turn running to acheive concurrency.
GIL = (global interpreter lock), allows only one thread to hold the control of the Python interpreter
"""

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finish studying")

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

print(threading.active_count())
print(threading.enumerate())
