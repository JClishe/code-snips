import random

word_list = ["ardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''  
+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''  
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

#pick a random work from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#create a list to hold the number of underscores equal to the number of letters in the chosen word
display = []
for letter in range(word_length):
    display.append("_")
    #display += "_" #this also works

end_of_game = False
lives = 6

while not end_of_game:
    #ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    #replace the underscores in the display list with the correctly guessed letter at the appropriate position
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

    if lives == 0:
        end_of_game = True
        print("You lose.")

