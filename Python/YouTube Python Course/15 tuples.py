#similar to lists but ordered and unchangeable. Used to group related data together

student = ("Jason", 47, "male")

#some methods available to tuples
print(student.count("Jason"))
print(student.index("male"))

#to display all contents in a tuple
for x in student:
    print(x)

#search a tuple
if "Jason" in student:
    print("Jason is here")
