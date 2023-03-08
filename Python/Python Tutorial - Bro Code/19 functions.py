#a function is a block of code which is executed only when it is called

def hello(): #this is how you define a function
    print("Hello")
    print("Have a nice day")

hello()

#Same as above, but we're going to pass an argument into the function
def hello(name): #name is the paramter that we're going to define with the argument passed into the function. This variable only exists within the function
    print("Hello "+name)
    print("Have a nice day")

hello("Jason") #Jason is the argument that we're passing into the function

#Same as above, but we're going to pass a variable into the function
def hello(name): #we're passing my_name into the function but naming it "name" within the function
    print("Hello "+name)
    print("Have a nice day")

my_name = "Jason"

hello(my_name) #my_name is the variable that we're passing into the function

print("===")

#Same as above, but we're going to pass multiple arguments into the function
def hello(first_name, last_name):
    print("Hello "+first_name+" "+last_name)
    print("Have a nice day")

first_name = "Jason"
last_name = "Clishe"

hello(first_name, last_name) #there needs to be a matching number of parameters in the function definition to receive the arguments we're sending into it