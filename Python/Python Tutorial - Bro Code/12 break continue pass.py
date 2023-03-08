#loop control statements. Used to change a loops execution from its normal sequence

#break =    used to terminate the loop
#continue = skips to the next iteration of the loop
#pass =     does nothing, acts as a placeholder

#loop only terminates when input isn't blank
"""
while True:
    name = input("Enter your name\n")
    if name != "":
        break 

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
"""

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
        