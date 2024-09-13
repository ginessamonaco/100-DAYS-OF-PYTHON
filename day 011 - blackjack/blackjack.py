import random

suits = ["of ♥", "of ⬧", "of ♣", "of ♠"]

card_numbers = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
              "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

card_numbers_dict = {
    "Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,"Seven": 7,
    "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10
}

def instructions():
    print("HOW TO PLAY:")
    print("You want to get as close to 21 as possible without going over.")
    print("Each number card is worth its number. Jack, Queen, and King cards are all worth 10. If you recieve an Ace card, it can be worth 1 or 11.")
    print("The dealer will deal a card to themselves and you, both face up.")
    print("Then the dealer will deal another card to themselves and you, their's will be face down, and yours will be face up.")
    print("You get to decide then if you would like to 'hit' and recieve another card, or 'finish' with your current cards.")
    print("If you go over 21 you lose. If the dealer is closer than you, you lose. If you both go over or have the same number, it's a draw.")
    print("If the dealer's first two cards add up to 16 or less, they automatically have to recieve another card.")
    print("Have fun!\n")


print("\nWelcome to Blackjack!")
start_game = input("\nEnter 'yes' to start playing, or 'no' to end the game: ").lower()

dealer_points = 0
player_points = 0

end_game = False

while not end_game:
    one_vs_one = (f"{dealer_points} / {player_points}")
    print("\nSCORE BOARD:\n(Dealer / You)")
    print(one_vs_one)

    if start_game == 'yes':
        print("\n")
        give_instructions = True
        
        while give_instructions:
            see_game_instructions = input("Enter 'yes' to see the game instructions, or 'no' to start playing: ").lower()
            print("\n")

            if see_game_instructions == "yes":
                instructions()
                give_instructions = False
            elif see_game_instructions == "no":
                give_instructions = False
            else:
                print("Invalid entry.\n")

        dealers_card_list = []
        players_card_list = []

        random_card1_number_player = random.choice(card_numbers)
        player_card1_number_value = card_numbers_dict[random_card1_number_player]
        random_card1_suit_player = random.choice(suits)
        player_final_card1 = random_card1_number_player + " " + random_card1_suit_player

        players_card_list += [player_final_card1]

        player_same_card2 = True

        while player_same_card2:
            random_card2_number_player = random.choice(card_numbers)
            player_card2_number_value = card_numbers_dict[random_card2_number_player]
            random_card2_suit_player = random.choice(suits)
            player_final_card2 = random_card2_number_player + " " + random_card2_suit_player
            if player_final_card2 not in dealers_card_list:
                if player_final_card2 not in players_card_list:
                    players_card_list += [player_final_card2]
                    player_same_card2 = False

        dealer_same_card1 = True

        while dealer_same_card1:
            random_card1_number_dealer = random.choice(card_numbers)
            dealer_card1_number_value = card_numbers_dict[random_card1_number_dealer]
            random_card1_suit_dealer = random.choice(suits)
            dealer_final_card1 = random_card1_number_dealer + " " + random_card1_suit_dealer
            if dealer_final_card1 not in dealers_card_list:
                if dealer_final_card1 not in players_card_list:
                    dealers_card_list += [dealer_final_card1]
                    dealer_same_card1 = False

        dealer_same_card2 = True

        while dealer_same_card2:
            random_card2_number_dealer = random.choice(card_numbers)
            dealer_card2_number_value = card_numbers_dict[random_card2_number_dealer]
            random_card2_suit_dealer = random.choice(suits)
            dealer_final_card2 = random_card2_number_dealer + " " + random_card2_suit_dealer
            if dealer_final_card2 not in dealers_card_list:
                if dealer_final_card2 not in players_card_list:
                    dealers_card_list += [dealer_final_card2]
                    dealer_same_card2 = False


        if player_card1_number_value == 1:
            if player_card2_number_value + 11 == 21:
                player_card1_number_value = 11
        elif player_card2_number_value == 1:
            if player_card1_number_value + 11 == 21:
                player_card2_number_value = 11
        elif dealer_card1_number_value == 1:
            if dealer_card2_number_value + 11 == 21:
                dealer_card1_number_value = 11
        elif dealer_card2_number_value == 1:
            if dealer_card1_number_value + 11 == 21:
                dealer_card2_number_value = 11

        print(f"Dealer's cards: [{dealer_final_card1}, (UNKNOWN)]")
        print(f"Your cards: [{player_final_card1}, {player_final_card2}] Your current Score: {player_card1_number_value + player_card2_number_value}")

        dealer_total_score = dealer_card1_number_value + dealer_card2_number_value
        player_total_score = player_card1_number_value + player_card2_number_value

        player_over = False
        hit = True

        while hit:
            if player_total_score < 21:
                hit_finish = input("\nEnter 'hit' to recieve another card, or 'finish' to settle with your current cards: ").lower()
                print("\n")
                if hit_finish == "finish":
                    hit = False
                elif hit_finish == "hit":
                    random_card0_number_player = random.choice(card_numbers)
                    player_card0_number_value = card_numbers_dict[random_card0_number_player]
                    random_card0_suit_player = random.choice(suits)
                    player_final_card0 = random_card0_number_player + " " + random_card0_suit_player

                    players_card_list += [player_final_card0]
                    player_total_score += player_card0_number_value

                    if player_card0_number_value == 1:
                        if (player_total_score - player_card0_number_value) + 11 == 21:
                            player_card0_number_value = 11
                            player_total_score -= 1
                            player_total_score += player_card0_number_value
                    elif player_card1_number_value == 1:
                        if (player_total_score - player_card1_number_value) + 11 == 21:
                            player_card1_number_value = 11
                    elif player_card2_number_value == 1:
                        if (player_total_score - player_card2_number_value) + 11 == 21:
                            player_card2_number_value = 11                    

                    print(f"Dealer's cards: [{dealer_final_card1}, (UNKNOWN)]")
                    print(f"Your cards: {players_card_list} Your current Score: {player_total_score}")
                    if player_total_score > 21:
                        player_over = True
                        hit = False
                else:
                    print("Invalid entry.\n")
            else:
                hit = False

        dealer_over = False
        dealer_add_card = True

        while dealer_add_card:
            if dealer_total_score < 17:
                random_card0_number_dealer = random.choice(card_numbers)
                dealer_card0_number_value = card_numbers_dict[random_card0_number_dealer]
                random_card0_suit_dealer = random.choice(suits)
                dealer_final_card0 = random_card0_number_dealer + " " + random_card0_suit_dealer
        
                dealers_card_list += [dealer_final_card0]
                dealer_total_score += dealer_card0_number_value

                if dealer_card0_number_value == 1:
                    if (dealer_total_score - dealer_card0_number_value) + 11 == 21:
                        dealer_card0_number_value = 11
                        dealer_total_score -= 1
                        dealer_total_score += dealer_card0_number_value
                elif dealer_card1_number_value == 1:
                    if (dealer_total_score - dealer_card1_number_value) + 11 == 21:
                        dealer_card1_number_value = 11
                elif dealer_card2_number_value == 1:
                    if (dealer_total_score - dealer_card2_number_value) + 11 == 21:
                        dealer_card2_number_value = 11

            elif dealer_total_score == 21:
                dealer_add_card = False
            elif dealer_total_score > 21:
                dealer_over = True
                dealer_add_card = False
            elif 16 < dealer_total_score < 21:
                dealer_over = False
                dealer_add_card = False

        dealer_battles_player = True

        while dealer_battles_player:
            if dealer_total_score < 21:
                if dealer_total_score < player_total_score:
                    random_card3_number_dealer = random.choice(card_numbers)
                    dealer_card3_number_value = card_numbers_dict[random_card3_number_dealer]
                    random_card3_suit_dealer = random.choice(suits)
                    dealer_final_card3 = random_card3_number_dealer + " " + random_card3_suit_dealer
            
                    dealers_card_list += [dealer_final_card3]
                    dealer_total_score += dealer_card3_number_value

                    if dealer_card3_number_value == 1:
                        if (dealer_total_score - dealer_card3_number_value) + 11 == 21:
                            dealer_card3_number_value = 11
                            dealer_total_score -= 1
                            dealer_total_score += dealer_card3_number_value
                    elif dealer_card1_number_value == 1:
                        if (dealer_total_score - dealer_card1_number_value) + 11 == 21:
                            dealer_card1_number_value = 11
                    elif dealer_card2_number_value == 1:
                        if (dealer_total_score - dealer_card2_number_value) + 11 == 21:
                            dealer_card2_number_value = 11
                    elif dealer_card0_number_value == 1:
                        if (dealer_total_score - dealer_card0_number_value) + 11 == 21:
                            dealer_card0_number_value = 11

                elif dealer_total_score > player_total_score:
                    dealer_battles_player = False

            elif dealer_total_score == 21:
                dealer_battles_player = False
            elif dealer_total_score > 21:
                dealer_over = True
                dealer_battles_player = False
            elif 16 < dealer_total_score < 21:
                dealer_over = False
                dealer_battles_player = False
        
        print("\nDEALER'S CARDS:")
        for dc in dealers_card_list:
            print(dc)

        print("\nYOUR CARDS:")
        for pc in players_card_list:
            print(pc)

        if player_over == True:
            if dealer_over == True:
                print(f"\n[Dealer: {dealer_total_score} / Player {player_total_score}]\n\nYou both went over 21.\nDRAW")
            else:
                print(f"\n[Dealer: {dealer_total_score} / Player {player_total_score}]\n\nYou went over 21.\nYOU LOST")
                dealer_points += 1
        elif player_over == False:
            if dealer_over == True:
                print(f"\n[Dealer: {dealer_total_score} / Player {player_total_score}]\n\nDealer went over 21.\nYOU WON")
                player_points += 1
            elif dealer_total_score == player_total_score:
                print(f"\n[Dealer: {dealer_total_score} / Player {player_total_score}]\n\nYou both got the same score.\nDRAW")
            elif player_total_score > dealer_total_score:
                print(f"\n[Dealer: {dealer_total_score} / Player {player_total_score}]\n\nYour score was closer to 21.\nYOU WON")
                player_points += 1
            else:
                print(f"\n[Dealer: {dealer_total_score} / Player {player_total_score}]\n\nDealer's score was closer to 21.\nYOU LOST")
                dealer_points += 1
        
        play_again_question = True

        while play_again_question:
            play_again = input("\nEnter 'yes' to play again, or 'no' to end the game: ").lower()
            if play_again == "no":
                end_game = True
                play_again_question = False
            elif play_again == "yes":
                play_again_question = False
            else:
                print("Invalid Entry.")

    elif start_game == 'no':
        end_game = True


one_vs_one = (f"{dealer_points} / {player_points}")
print("\nSCORE BOARD:\n(Dealer / You)")
print(one_vs_one)

print("\nGAME ENDED\n")