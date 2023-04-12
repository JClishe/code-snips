import random
from day_06_hangman_word_list import word_list
from day_06_hangman_art import stages
 
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
guessed_letters = []

while not end_of_game:
    #ask the user to guess a letter
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You have already chosen that letter, please guess again")
        guessed_letters.append(guess)
    else:
    #replace the underscores in the display list with the correctly guessed letter at the appropriate position
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        #deduct a life if the user chooses a letter that's not in the chosen word
        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            print("The letter you guessed is not in the chosen word, you lose a life. Please guess again")
        guessed_letters.append(guess)

    print(f' '.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win.")

    if lives == 0:
        end_of_game = True
        print("You lose.")

