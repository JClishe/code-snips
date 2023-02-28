calculation_to_units = 24 * 60 * 60
name_of_unit = "seconds"

#DEFINE A FUNCTION
def days_to_units():
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
    print("All good!")

days_to_units() #Defining a function doesn't actually do anything with it. We need to call it in order to run it

#PASS A VARIABLE INTO THE FUNCTION
def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print("All good!")

days_to_units(35)

#PASS MULTIPLE VARIABLES INTO THE FUNCTION
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

days_to_units(35, "Awesome!")