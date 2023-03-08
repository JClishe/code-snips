import random

"""
choices = ["rock","paper","scissors"]

computer = random.choice(choices)

player = input("rock, paper, or scissors: ")

print("Computer: ",computer)
print("Player: ",player)


#we need to prevent the player from entering any random text and sticking to our options
choices = ["rock","paper","scissors"]

computer = random.choice(choices)

player = None #the player variabe needs to be initialized first in order to use it in the while loop below

while player not in choices:
    player = input("rock, paper, or scissors: ").lower() #this will keep looping until the player enters one of the options. Also, since the choices are case sensitive, we need to use the lower method to make the inpot lower case in case the player uses capitalization 

if player == computer:
    print("Computer: ",computer)
    print("Player: ",player)
    print("Tie!")
elif player == "rock":
    if computer == "paper":
        print("Computer: ",computer)
        print("Player: ",player)
        print("You lose!")
    if computer == "scissors":
        print("Computer: ",computer)
        print("Player: ",player)
        print("You win!")
elif player == "scissors":
    if computer == "rock":
        print("Computer: ",computer)
        print("Player: ",player)
        print("You lose!")
    if computer == "paper":
        print("Computer: ",computer)
        print("Player: ",player)
        print("You win!")
elif player == "paper":
    if computer == "scissors":
        print("Computer: ",computer)
        print("Player: ",player)
        print("You lose!")
    if computer == "rock":
        print("Computer: ",computer)
        print("Player: ",player)
        print("You win!")
"""

#to ask the user if they want to play again, we can put the entire game code inside of a while loop
while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("rock, paper, or scissors: ").lower()

    if player == computer:
        print("Computer: ",computer)
        print("Player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!")
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!")
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You lose!")
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("You win!")

    play_again = input("Would you like to play again (yes/no)?: ").lower()

    if play_again != "yes":
        break

print("Bye!")
