import os

path = "/Users/jasonclishe/downloads/WF3640_Lite_64NR_NA.dmg"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That location is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist")