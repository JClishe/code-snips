#used to pass values/objects back to the caller. These values/objects are known as the functions return value

def multiply(number1,number2):
    result = number1 * number2
    return result

x = multiply(6,8)

print(x)

#another way to write the same code
def multiply(number1,number2):
    return number1 * number2

x = multiply(6,8)

print(x)