import random

word_list = ["miscellaneous", "acquaintance", "entrepreneur", "unacceptable", "fraudulently",
             "procrastinate", "contaminate", "underprivileged", "fundamental", "decaffeinated",
             "inconsequential", "biodegradable", "optimistically", "narcissistic", "counterattack",
             "circumference", "fluorescent", "uncooperative", "sophisticated", "refurbishment",
             "disingenuous", "occupational", "exaggeration", "misdemeanour", "perpendicular"]

stages = ['''
    _______
   |/      |
   |      
   |      
   |       
   |      
   |
___|___
''', '''
    _______
   |/      |
   |      (_)
   |      
   |       
   |      
   |
___|___
''', '''
    _______
   |/      |
   |      (_)
   |       |
   |       |
   |      
   |
___|___
''', '''
    _______
   |/      |
   |      (_)
   |      \|
   |       |
   |      
   |
___|___
''', '''
    _______
   |/      |
   |      (_)
   |      \|/
   |       |
   |      
   |
___|___
''', '''
    _______
   |/      |
   |      (_)
   |      \|/
   |       |
   |      / 
   |
___|___
''', '''
    _______
   |/      |
   |     (X_X) 
   |      \|/
   |       |
   |      / \ 
   |
___|___
''']


print("\nWelcome to hangman.")
random_word = random.choice(word_list)
word_length = len(random_word)


space_list2 = []

for letter in random_word:
    letter = "_"
    space_list2.append(letter)
print("\nThe word is:")
print(*space_list2)
print(f"Guesses remaining: 6")

game_over = False

wrong_letters = []
lives = 6
stage = 0

while not game_over:
    print(stages[stage])
    print(f"Past wrong guesses:")
    print(*wrong_letters, sep = " ")
    guess = input("Guess a letter: ").lower()

    length = 0
    wrong = 0

    while length < word_length:
        if guess == random_word[length]:
            space_list2[length] = guess
        elif guess != random_word[length]:
            wrong += 1
        length += 1
    print("The word is:")
    print(*space_list2, sep = " ")
    print(f"Guesses remaining: {lives}")

    if wrong == word_length:
        lives -= 1
        stage += 1
        wrong_letters.append(guess)
        print(f"\nGuesses remaining: {lives}")

    if lives < 1:
        game_over = True
        print(stages[stage])
        print(f"The word was: {random_word}")
        print("Your stick man was hung. You lose!")

    if "_" not in space_list2:
        game_over = True
        print(f"The word is {random_word}. You win!")
