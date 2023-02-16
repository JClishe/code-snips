#exception is an event detected during execution that interrupts the flow of a program
#use a try block to execute code that might be considered dangerous, such as when accepting user input and we don't know what they may type

#if we run this and divide 5 by 0, we'll get an exception
"""
numerator = int(input("Enter a number to divide: "))
denominator = int(input("Enter a number to divide by: "))
result = numerator / denominator
print(result)

#wrap the above code in a try block
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError: #this catches the error created by dividing by zero
    print("You can't divide by zero")
except ValueError: #this catches errors created by entering a non-integer value, such as 5 divided by pizza
    print("Please enter numbers only")
except Exception: #this catches all other exceptions
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute") #optional, but anything in a finally statement will always execute even if there was an exception. Common if you need close a file
"""

#we can also print the exception error so the user can see it
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e: #"e" is commonly used but can be anything
    print(e)
    print("You can't divide by zero")
except ValueError as e:
    print(e)
    print("Please enter numbers only")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")


