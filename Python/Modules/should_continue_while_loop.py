should_continue = True

while should_continue is True: #"is True" isn't actually necessary but makes it easier to read
    #do some stuff
    ...

    if input(f"Type 'y' to continue or type 'n' to exit: ").lower() == "y":
        ...
    else:
        should_continue = False