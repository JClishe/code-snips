"""
A thread that runs in the background, not important for program to run. Your program will not wait for daemon threads to complete before exiting. Non-daemon threads cannot normally be killed, they stay alive until the task is complete
ex. background tasks, garbage collection, waiting for input, running long processes
"""

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"logged in for {count} seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do you wish to exit?")
