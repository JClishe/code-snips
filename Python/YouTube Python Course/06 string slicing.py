#create a substring by extracting elements from another string by using index operator or slice function
#indexing = [start:stop:step]

name = "Jason Clishe" 

#slice the name variable to extract elements into another variable
first_name = name[0:5] #starting index position:stopping index position. Start position INCLUDES the position index, stopping position EXCLUDES the position index. So our stopping position needs to be one position past the final position that we want to include. Can optionally omit the starting position if starting at 0 ie., [:5]
last_name = name[6:12] #can optionally omit the stopping position to include everything after the starting position ie., [6:]
funky_name = name[0:12:2] #step count of 2 only captures every other position

print(first_name)
print(last_name)
print(funky_name)

#using a negative step count will count backwards
reversed_name = name[::-1]
print(reversed_name)

#use the slice function to perform a similar outcome
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) #slicing using same start and stop position as index. However, in this case we want to count from the right for the stop position

print(website1[slice])
print(website2[slice])


