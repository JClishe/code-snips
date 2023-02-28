#basically the same code as above but error handling is handled via try/except. This makes it easier to catch invalid input instead of defining each invalid input possibility
calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(int(user_input))
            print(calculated_value)
        elif user_input_number == 0:
                print("You entered a 0, please enter a positive number")
        else:
            print("Enter a positive number only")
    except ValueError: #Enter the type of error you want to catch, or leave blank to catch all errors
        print("Please enter a whole number only")

user_input = input("Enter number of days to be converted\n") 
validate_and_execute()