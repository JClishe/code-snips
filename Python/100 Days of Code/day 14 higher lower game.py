import random
from day_14_art import logo, vs
#from day_14_art import vs
from day_14_game_data import data

option_a = (random.choice(data))
option_b = (random.choice(data))

score = 0

should_continue = True

while should_continue is True:
    print(logo)
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

    #Set the users selection to the appropriate star
    user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_selection == 'a':
        user_selection = option_a
    elif user_selection == 'b':
        user_selection = option_b

    #Determine which option has a higher follower count
    bigger_star = 0
    if option_a['follower_count'] > option_b['follower_count']:
        bigger_star = option_a
    else:
        bigger_star = option_b

    #Determine if the user guessed correctly
    if user_selection == bigger_star:
        score += 1
        print(f"You're right! Current score: {score}")
        option_a = option_b
        option_b = (random.choice(data))
        should_continue = True
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False

