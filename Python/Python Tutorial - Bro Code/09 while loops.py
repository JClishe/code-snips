#statement that will execute a block of code as long as its condition remains true

#prompt user for their name, do not allow them to not enter anything
"""
name = ""

while len(name) == 0:
    name = input("Enter your name\n")

print("Hello "+name)
"""

#another way of writing the same statement
name = None 

while not name:
    name = input("Enter your name\n")

print("Hello "+name)
