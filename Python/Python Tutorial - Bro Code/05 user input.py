#user inputs are always captured as strings

name = input("What is your name? ")

#cast a user input to another data type
age = int(input("How old are you? "))

#now we can use the age for other operations if needed
age = age + 1

#if we want to print the value of age within a string, we need to cast it back to a string for string concatenation
print("Hello "+name)
print("You are "+str(age)+" years old")
