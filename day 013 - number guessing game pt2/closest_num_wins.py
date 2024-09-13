guesses = {}

keys = list(guesses.keys())
values = list(guesses.values())

the_number = int(input("Enter the number to be guessed (1-100): "))

guessing_finished = False

while guessing_finished == False:
    print("Enter the number you think was chosen.\nWhoever has the closest guess without going over wins.")
    guessers_name = input("Enter your name: ").lower()

    diff_choice = False

    while not diff_choice:
        guessers_choice = int(input("Enter your guess (1-100): "))
        if guessers_choice not in values:
            values += [guessers_choice]
            print(values)
            diff_choice = True
        else:
            print(f"\nSomebody already guessed {guessers_choice}. Pick a different number.")

    guesses[guessers_name] = guessers_choice

    any_other_guessers = input("Are there any other guessers? (Type 'yes' or 'no'): ").lower()

    if any_other_guessers == "no":
        guessing_finished = True
    else:
        print("\n" * 100)

def find_winning_number():
    winning_number = max(final_values)
    win_num_location = final_values.index(winning_number)
    winning_guesser = final_keys[win_num_location]

    print(f"\n{(winning_guesser).upper()} guessed {winning_number} which is the closest to {the_number} without going over.\n")

end_game = False
x = 0

while not end_game:
    closest_numbers = {}
    for g in guesses:
        if guesses[g] == the_number:
            print(f"\n{(g).upper()} won. They guessed the exact number: {guesses[g]}")
            x += 1
            end_game = True
        elif guesses[g] < the_number:
            closest_numbers[g] = guesses[g]
    
    end_game = True

if x == 0:
    final_keys = list(closest_numbers.keys())
    final_values = list(closest_numbers.values())

    find_winning_number()