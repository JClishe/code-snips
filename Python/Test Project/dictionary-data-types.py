#Allow user to choose conversion type instead of always days to hours
#Dictionary converts data to a key:value pair
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Unsupported unit"

def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
                print("You entered a 0, please enter a positive number")
        else:
            print("Enter a positive number only")
    except ValueError: #Enter the type of error you want to catch, or leave blank to catch all errors
        print("Please enter a whole number only")

user_input = "" #assign an empty string to the user_input variable so the while loop has something to evaluate on its first run
while user_input != "exit":
    user_input = input("Enter number of days and conversion unit, expressed as days:units (ex:10:hours)\n") 
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()