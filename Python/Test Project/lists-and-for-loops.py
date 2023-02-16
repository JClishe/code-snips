calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(int(user_input_number))
            print(calculated_value)
        elif user_input_number == 0:
                print("You entered a 0, please enter a positive number")
        else:
            print("Enter a positive number only")
    except ValueError: #Enter the type of error you want to catch, or leave blank to catch all errors
        print("Please enter a whole number only")

user_input = "" #assign an empty string to the user_input variable so the while loop has something to evaluate on its first run
while user_input != "exit":
    user_input = input("Enter number of days as a comma seperated list to be converted to hours\n") 
    for num_of_days_element in user_input.split(","):
        validate_and_execute()