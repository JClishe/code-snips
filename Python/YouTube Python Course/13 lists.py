#lists store multiple items within a single variable

food = ["pizza", "hamburger", "hotdog"]

#print the entire variable
print(food)

#to print a specific element in the list, use its index number
print(food[0])

#replace an element in the list
food[1] = "sushi"
print(food)

#to print every element in a list

for x in food:
    print(x)

#use the append function to add an element to a list
food.append("ice cream")
print(food)

#use the remove function to remove an element from a list
food.remove("hotdog")
print(food)

#use pop function to remove the last element
food.pop()
print(food)

#insert an element at a specific index position
food.insert(1, "cake")
print(food)

#sort a list alphabetically
food.sort()
print(food)

#clear a list
food.clear()
print(food)
