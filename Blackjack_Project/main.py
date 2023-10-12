from art import logo
import random
print(logo)


def player_add_card():
    player_card.append(cards[random.randint(0, len(cards)-1)])


def dealer_add_card():
    dealer_cards.append(cards[random.randint(0, len(cards)-1)])


def start_game():
    player_add_card()
    dealer_add_card()
    dealer_add_card()


def end_game(c_player, t_player, c_dealer, t_dealer) :
    print("")
    print("")
    print(f"Your final hand: {c_player}, final score: {t_player}")
    print(f"Computer's final hand: {c_dealer}, final score: {t_dealer}")

    if t_player > 21:
        print("You went over. \nYou Lose.")
    print("")
    print("")
    return False


new_game = True
stand = True
while new_game:
    keep_playing = input("Do you  want to play a game of Blackjack? Type 'y' or 'n': ")

    if keep_playing == 'y':
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        player_card = []
        dealer_cards = []
        stand = True

        start_game()
        while stand:
            player_add_card()
            player_total = 0
            dealer_total = 0

            for i in player_card:
                player_total += i

            for i in dealer_cards:
                dealer_total += i

            if player_total < 21:
                print(f"Your cards are {player_card}, your total is: {player_total}")
                print("Dealer's first card: ", dealer_cards[0])
                hit = input("Type 'y' to get another card, type 'n' to pass: ")

                if hit == "n":

                    if dealer_total < 17:
                        dealer_add_card()
                        dealer_total = 0
                        for i in dealer_cards:
                            dealer_total += i
                    end_game(player_card, player_total, dealer_cards, dealer_total)

                    if player_total > dealer_total:
                        print("YOU WIN!!!")
                    elif player_total == dealer_total:
                        print("PUSH!!!")
                    elif player_total < dealer_total:
                        print("You Lose")
                    break

            elif player_total > 21:
                stand = end_game(player_card, player_total, dealer_cards, dealer_total)
    else:
        print("Thanks for playing!")
        new_game = False
















