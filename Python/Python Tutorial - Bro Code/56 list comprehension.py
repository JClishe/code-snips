"""
A way to create a new list with less syntax. can mimic certain lambda functions, easier to read
list = [expression for item in iterable]
list = [expression for item in iterable if conditional]
list = [expression if/else for item in iterable]
"""

#traditional example, this will print the square root of all numbers 1 through 10
squares = []
for i in range(1,11):
    squares.append(i * i)
print(squares)

#here's another way to perform the same operation using list comprehension
squares = [i * i for i in range(1,11)] #expression is i * 1, for item is for i in range, iterable is 1,11
print(squares)

#traditional method of filtering a list above a certain value
students = [100,90,80,70,60,50,40,30,20,10,0]
passed_students = list(filter(lambda x: x >=60, students))
print(passed_students)

#another way to write the same operation but with list comprehension
passed_students = [i for i in students if i >= 60]
print(passed_students)

#another version but with an ef/else statement
passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)