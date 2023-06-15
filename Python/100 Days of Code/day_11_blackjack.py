import random

new_game = True

while new_game is True:
    def deal_card():
        """Returns a random card from the deck."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card_dealt = random.choice(cards)
        return card_dealt

    computer_cards = []
    player_cards = []

    for _ in range(2): #runs the for loop twice to deal 2 cards to each player
        computer_cards.append(deal_card())
        player_cards.append(deal_card())

    def calculate_score(cards):
        """Adds the total cards in the hand"""
        return sum(cards)

    print(f"The computer drew {computer_cards[0]}")

    should_continue = True

    while should_continue is True:
        print(f"The player drew {player_cards}")

        if calculate_score(computer_cards) == 21:
            print("Computer scored a Blackjack, game over.")
            break
        elif calculate_score(player_cards) == 21:
            print("The player scored a Blackjack, game over.")
            break
        elif calculate_score(player_cards) > 21:
            if 11 in player_cards:
                for card in range(len(player_cards)):
                    if player_cards[card] == 11:
                        player_cards[card] = 1
            else:
                print("The player busted.")
                break

        if input(f"Type 'y' to draw another card or type 'n' to stand: ").lower() == "y":
            player_cards.append(deal_card())
        else:
            should_continue = False

    if calculate_score(player_cards) < 21:
        while calculate_score(computer_cards) <= 16:
            computer_cards.append(deal_card())

    print("\n")
    print(f"Computers hand: {computer_cards}")
    print(f"Players hand: {player_cards}")
    print(f"Final score: Computer: {calculate_score(computer_cards)}, Player: {calculate_score(player_cards)}")

    if calculate_score(computer_cards) > 21:
        print("Player wins")
    elif calculate_score(player_cards) > 21:
        print("Computer wins")
    elif calculate_score(computer_cards) == calculate_score(player_cards):
        print("Draw")
    elif calculate_score(computer_cards) > calculate_score(player_cards):
        print("Computer wins")
    else:
        print("Player wins")

    if input(f"Type 'y' if you'd like to play another game or type 'n' to quit: ").lower() == "y":
        new_game = True
        print("\n")
    else:
        new_game = False