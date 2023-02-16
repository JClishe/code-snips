#a block of code that executes only if its condition is true

age = int(input("How old are you\n"))

if age == 100:
    print("You are a century old")
elif age >= 18:
    print("You are an adult")
elif age <0: #can be additional else if statements as required
    print("You haven't been born yet")
else: #else is the condition of last resort that catches any conditions not met by any other statement
    print("You are a child")


