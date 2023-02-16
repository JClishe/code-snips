#loop inside of a loop. The "inner" loop will finish all of its iterations before finishing one iteration of the "outer" loop that contains it

rows = int(input("How many rows?\n"))
columns = int(input("How many columns?\n"))
symbol = input("Enter a symbol to use\n")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #the end statement prevents the cursor from moving to the next line
    print()

    