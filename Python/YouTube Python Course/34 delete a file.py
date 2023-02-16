import os

path = "34 test.txt"

#os.remove(path)

try:
    os.remove(path)
except FileNotFoundError:
    print("File not found")


