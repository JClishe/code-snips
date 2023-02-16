#sets are collections which are unorderedd and unindexed. Sets do not allow duplicate values

utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup"}

for x in utensils:
    print(x)

print("=====")

#common methods
utensils.add("napkin")
utensils.remove("fork")

for x in utensils:
    print(x)

print("====")

#add the contents of one set to another set
dishes.update(utensils)
print(dishes)

for x in dishes:
    print(x)

print("===")

#join 2 sets to create a new set
dinner_table = utensils.union(dishes)
for x in dinner_table:
    print(x)

#compare the difference between 2 sets
print(dishes.difference(utensils))

utensils.clear()

for x in utensils:
    print(x)
