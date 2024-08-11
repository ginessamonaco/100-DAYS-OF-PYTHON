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
# print(f"Shh... the word is {random_word}.")
word_length = len(random_word)


space_list2 = []

for letter in random_word:
    letter = "_"
    space_list2.append(letter)
print("\nThe word is:")
print(*space_list2)

game_over = False

lives = 6
stage = 0

while not game_over:
    print(stages[stage])
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

    if wrong == word_length:
        lives -= 1
        stage += 1
        print(f"\nUh oh... only {lives} chances left.")

    if lives < 1:
        game_over = True
        print(stages[stage])
        print("Your stick man was hung. You lose!")

    if "_" not in space_list2:
        game_over = True
        print(f"The word is {random_word}. You win!")