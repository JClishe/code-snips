#apply a function to an iterable and reduce it to a single cumulative value. Performs functions on first two elements and repeats process until 1 value remains

#reduce(function, iterable)

import functools

#the reduce function is combining the first 2 iterables of the letters list and repeating until there is only 1 iterable remaining. Very similar to a for loop
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)

#this is multiplying the first 2 numbers and repeating. Ex 5 * 4 = 20, 20 * 3 = 60; 60 * 2 = 120; 120 * 1 = 120
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y,:x * y,factorial)
print(result)

