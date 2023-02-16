def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "Unsupported unit"

def validate_and_execute(days_and_unit_dictionary): #We need to pass in the days_and_unit_dictionary variable from ModulesMain.py
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

user_input_message = "Enter number of days and conversion unit, expressed as days:units (ex:10:hours)\n"
