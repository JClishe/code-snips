#functions written in 1 line using lambda keyword. Accepts any number of arguments, but only has one expression.
#think of it as a shortcut
#useful if needed for a short period of time, throw-away

#lambda parameters:expression

#normal function
def double(x):
    return x * 2

print(double(5))

#same function written as lambda function
double = lambda x:x * 2
print(double(5))

#another example, with 2 arguments
multiply = lambda x, y:x * y
print(multiply(5,6))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Jason","Clishe"))

age_check = lambda age:True if age >= 18 else False
print(age_check(17))
