calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"

user_input = input("Enter number of days to be converted\n") 
#input is the built-in function, user_input is the variable we're assigning to it, and \n adds a new line

#input is always treated as a string. Use the built-in Int function to turn it into an integer (called Casting)
user_input_number = int(user_input)

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

calculated_value = days_to_units(user_input_number)
print(calculated_value)