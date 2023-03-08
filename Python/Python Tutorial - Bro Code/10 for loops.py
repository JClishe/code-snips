#statement that will execute its block of code a limited amount of times

"""
for i in range(10):
    print(i)
"""

for i in range(50,100+1,2): #the "2" indicates the step count. See the "06 string slicing" file for more details
    print(i)

import time

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
