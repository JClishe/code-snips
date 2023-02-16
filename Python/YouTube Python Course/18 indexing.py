#index operator [] gives access to a sequence's element (str, list, tuples)

name = "jason clishe"

if(name[0].islower()):
    name = name.capitalize()

print(name)

first_name = name[0:5].upper() #more details on this command in the 06 string slicing file

print(first_name)