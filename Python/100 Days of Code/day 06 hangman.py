import random

word_list = ["ardvark", "baboon", "camel"]

#pick a random work from the word list
chosen_word = random.choice(word_list)

#create a list to hold the number of underscores equal to the number of letters in the chosen word
display = []

for letter in range(len(chosen_word)):
    display.append("_")
    #display += "_" #this also works

print(display)

#ask the user to guess a letter
guess = input("Guess a letter: ").lower()

#replace the underscores in the display list with the correctly guessed letter at the appropriate position
position = 0
for letter in chosen_word:
    if letter == guess:
        display[position] = letter
        position += 1
    else:
        position += 1

print(display)