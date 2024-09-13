import random 

def higher_lower():
    return """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/  

"""

def vs():
    return """
 _ _ __ 
| | / _|
| V \_ \ 
 \_/|__/

"""

icons = [
    "@instagram", "@cristiano", "@leomessi", "@selenagomez",
    "@kyliejenner", "@therock", "@arianagrande", "@kimkardashian",
    "@beyonce", "@khloekardashian", "@nike", "@justinbieber",
    "@kendalljenner", "@taylorswift", "@virat.kohli", "@natgeo",
    "@jlo", "@nickiminaj", "@kourtneykardashian", "@neymarjr"
]
icon_following = {
    "@instagram": 676, "@cristiano": 637, "@leomessi": 504, "@selenagomez": 425,
    "@kyliejenner": 398, "@therock": 396, "@arianagrande": 377, "@kimkardashian": 361,
    "@beyonce": 316, "@khloekardashian": 307, "@nike": 304, "@justinbieber": 293,
    "@kendalljenner": 292, "@taylorswift": 283, "@virat.kohli": 270, "@natgeo": 281,
    "@jlo": 251, "@nickiminaj": 228, "@kourtneykardashian": 222, "@neymarjr": 224,
}

end = False

points = 0
plays = 0

while not end:
    first_icon = random.choice(icons)

    choosing_second_icon = True

    while choosing_second_icon:
        second_icon = random.choice(icons)

        if second_icon != first_icon:
            choosing_second_icon = False
    
    print(higher_lower())

    score = (f"SCORE: {points} / {plays}")

    print(score)
    print(f"Icon A: {first_icon}")
    print("""
         _ _ __ 
        | | / _|
        | V \_ \ 
         \_/|__/
          
          """)
    print(f"Icon B: {second_icon}")

    first_icon_num = icon_following[first_icon]
    second_icon_num = icon_following[second_icon]

    finish_guessing = False

    while not finish_guessing:
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess != "A" and guess != "B":
            print("Invalid Entry.")
        else:
            finish_guessing = True

    if first_icon_num > second_icon_num:
        higher_person = first_icon
    elif first_icon_num < second_icon_num:
        higher_person = second_icon
    
    if guess == "A":
        if higher_person == first_icon:
            points += 1
            plays += 1
            print("CORRECT!")
        else:
            plays += 1
            print("WRONG!")
    else:
        if higher_person == second_icon:
            points += 1
            plays += 1
            print("CORRECT!")
        else:
            plays += 1
            print("WRONG!")

    question_play_again = True

    while question_play_again:
        play_again = input("Do you want to play again? 'y' or 'n': ").lower()

        if play_again == "n":
            question_play_again = False
            end = True
        elif play_again != "y" and play_again != "n":
            print("Invalid Response.")
        else:
            question_play_again = False

print("\nGame Ended\n")