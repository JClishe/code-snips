# walrus operator :=

#new to Python 3.8
#assignment expression aka walrus operator. Assigns values to variables as part of a larger expression

happy = True
print(happy)

print(happy := True) #this single line combines both previous lines

#==========
"""
foods = list()
while True:
    food = input("What food do you like?\n")
    if food == "quit":
        break
    foods.append(food)
"""

#now write the same program as above but using a walrus operator
foods = list()
while food := input("What food do you like?\n") != "quit":
    foods.append(food)


