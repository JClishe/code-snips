#the format method is available to strings and gives users more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)

print("===")

#repeat above using the format method
print("The {} jumped over the {}".format(animal,item)) #we're using the format method to pass variables into the string using position arguments denoted by curly braces

#same as above but using index values to define which argument is inserted at which location
print("The {0} jumped over the {1}".format(animal,item)) 

#another way, using keyword arguments instead of positional or index arguments
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))

#another way
text = "The {} jumped over the {}"
print(text.format(animal,item))

