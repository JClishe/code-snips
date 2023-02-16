#used to check whether 2 or more conditional statements are true (and, or, not)

temp = int(input("What is the temperature outside?\n"))

if temp >= 50 and temp <= 89:
    print("The temperature is good, go outside")
elif temp < 50 or temp >= 90:
    print("The temperature is bad, stay inside")

#not logical operator will flip a statement from false to true and vice versa
"""
if not(temp >= 50 and temp <= 89):
    print("The temperature is good, go outside")
elif not(temp < 50 or temp >= 90):
    print("The temperature is bad, stay inside")
"""