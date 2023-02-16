#read the contents of a file
"""
with open('30_test.txt') as file: #don't need a path since file is in same folder as project
    print(file.read())
"""

#could be better to put the above code into a try except block to handle file not found and other errors
try:
    with open('30_test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")
