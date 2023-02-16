#Import all logic, functions, variables, etc. from ModulesHelper.py into this file. Anything imported from another file is referred to as a Definition.
import ModulesHelper

"""
If we only wanted to import a specific function or variable from another file, we could use the following command instead of the previous import command. If we did this, we could reference it directly in this file as validate_and_execute instead of ModulesHelper.validate_and_execute
from ModulesHelper import validate_and_execute

We could also use a * to import all definitions from another file as seen below. This works basically the same as "import ModulesHelper", but any definitions imported this way would not need to be references as ModulesHelper.[definition]. It boils down to personal preference.
from ModulesHelper import *
"""

user_input = "" #assign an empty string to the user_input variable so the while loop has something to evaluate on its first run
while user_input != "exit":
    user_input = input(ModulesHelper.user_input_message) 
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    ModulesHelper.validate_and_execute(days_and_unit_dictionary) 
    #Reference any functions, variables, etc. from ModulesHelper.py by using modulename. then the name of the function or variable
    #The Import command is one-way. Helper doesn't know anything about functions and variables contained within this file, so we're passing days_and_unit_dictionary variable into the call to the validate_and_execute function 