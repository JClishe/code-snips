#function calls inside other function calls. The innermost calls are resolved first. The returned value is used as an argument for the next outer function

#if you enter a decimal number at the prompt below, it will iterate through the functions to eventually convert it to a positive whole number
num = input("Enter a whole positive number:\n")
num = float(num)
num = abs(num)
num = round(num)
print(num)

#the same command can be written in one line of code
print(round(abs(float(input("Enter a whole positive number:\n")))))
