
#GLOBAL VARIABLES
#These variable are needed for all sections prior to the Dictionary Data Types section
#calculation_to_units = 24 * 60 * 60
#name_of_unit = "seconds"

"""print(f"20 days are {20 * calculation_to_units} {name_of_unit}")

#USE CONDITIONALS TO VALIDATE USER INPUT
def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "Please enter a non-zero value"
    else:
        return "Please enter a positive value" #This technically isn't needed, the isdigit function below will filter for zero's

def validate_and_execute():
    if user_input.isdigit():
        calculated_value = days_to_units(int(user_input))
        print(calculated_value)
    else:
        print("Please enter a whole number only")

user_input = input("Enter number of days to be converted\n") 
validate_and_execute()

#NESTED IF ELSE
#this is the same code as above, just reorganized to place all the validation logic within a single nested if else statement
def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(int(user_input))
            print(calculated_value)
        elif user_input_number == 0:
                print("You entered a 0, please enter a positive number")
    else:
        print("Please enter a whole number only")

user_input = input("Enter number of days to be converted\n") 
validate_and_execute()

"""
