import os

source = "33_test.txt"
destination = "/Users/jasonclishe/desktop/test.txt"

#put command inside try except block in case file does not exist
try:
    if os.path.exists(destination):
        print("There is already a file in the destination with this name")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
