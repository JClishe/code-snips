import random

choice = input("Do you choose Rock, Paper, or Scissors? ").lower()

list = ["rock", "paper", "scissors"]
computer_choice = list[random.randint(0,2)]

print(f"Computer chooses {computer_choice}")

if choice == "rock":
    if computer_choice == "rock":
        print("Tie")
    elif computer_choice == "paper":
        print("You lose")
    else:
        print("You win!")
elif choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    elif computer_choice == "paper":
        print("Tie")
    else:
        print("You lose")
elif choice == "scissors":
    if computer_choice == "rock":
        print("You lose")
    elif computer_choice == "paper":
        print("You win!")
    else:
        print("Tie")
else:
    print("You did not choose a valid option")

