import random

#Global constants are basically pre-defined variables that don't change
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

#The computer chooses a random number between 1 and 100
number = random.randint(1, 100)

def compare(guesses_remaining):
    for i in range(guesses_remaining):
        print(f"You have {guesses_remaining} attempts remaining to guess.")
        guess = int(input("Make a guess: \n")) #prompt the user to guess a number and store it in a variable called 'guess'

        if guess == number:
            print("You guessed the correct number!")
            break
        elif guess > number:
            print("Too high, guess again.")
        elif guess < number:
            print("Too low, guess again.")

        guesses_remaining -= 1 #decrement the remaining guesses by 1

        if guesses_remaining == 0:
            print("You lose.")

if difficulty == 'easy':
    compare(EASY_LEVEL_TURNS) #execute the compare function and give the user 10 attempts
elif difficulty == 'hard':
    compare(HARD_LEVEL_TURNS) #execute the compare function and give the user 5 attempts
else:
    print("You entered an invalid option.")
