#scope is the region that a variable is recognized. A variable is only available from inside the region that it is created

name = "Jason"

def display_name():
    name = "Clishe"
    print(name) #local scope; only available inside the function

display_name() #this will call the local name variable inside the function
print(name) #this will call the global name variable defined outside the function

