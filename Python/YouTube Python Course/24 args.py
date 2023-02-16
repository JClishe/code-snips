#parameter that will pack all arguments into a tuple. Useful so that functions can accept a varying number of arguments

"""
#this won't work because we're passing 3 arguments into the function but have only defined 2 positions in the function
def add(num1,num2):
    sum = num1 + num2
    return sum

print(add(1,2,3))
"""

print("===")

#same as above but using args to pack all arguments into a tuple that can be iterated through
def add(*args): #can name this whatever we want, it's the * that's important
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3))
