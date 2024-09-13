import random

print("\nWelcome to the Number Guessing Game!")

points = 0
games = 0

end_game = False

while not end_game:
    score = (f"\nSCORE: {points} / {games}")
    print(score)
    print("I am thinking of a number between 1 and 100.")

    random_number = random.randint(1, 100)

    valid_response = False

    while not valid_response:
        easy_hard = input("\nType 'easy' to play on easy mode, or 'hard' to play on hard mode: ").lower()

        if easy_hard == "easy":
            attempts = 10
            valid_response = True
        elif easy_hard == "hard":
            attempts = 5
            valid_response = True
        else:
            print("Invlaid Entry")


    no_more_tries = False

    while not no_more_tries:
        if attempts < 0:
            print(f"You ran out of attempts. The number was {random_number}.")
            games += 1
            no_more_tries = True

        elif attempts >= 0:
            print(f"You have {attempts} attempts left.")

            invalid_number = True

            while invalid_number:
                guess = int(input("Enter your guess here: "))

                if guess > 100:
                    print("You guessed a number over 100. The number is between 1 and 100.")
                elif guess < 1:
                    print("You guessed a number lower than 1. The number is between 1 and 100.")
                else:
                    invalid_number = False

            attempts -= 1

            if guess == random_number:
                print(f"You guessed the correct number! The number was {guess}.")
                points += 1
                games += 1
                no_more_tries = True
            elif guess > random_number:
                print("Your guess was too high. Guess a lower number.")
            elif guess < random_number:
                print("Your guess was too low. Guess a higher number.")

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()

    if play_again == "no":
        end_game = True

print(f"\nSCORE: {points} / {games}")
print("Game ended")
