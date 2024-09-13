import random 

player_choice = (int(input("What do you choose? Type 1 for Rock, 2 for Paper, or 3 for Scissors.\n"))) - 1
computer_choice = random.randint(0, 2)

rps = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

print(f"You Chose:\n{rps[player_choice]}")
print(f"Computer Chose:\n{rps[computer_choice]}")

if player_choice == computer_choice:
    print("YOU TIED!")
elif player_choice == 0 and computer_choice == 1:
    print("YOU LOST!")
elif player_choice == 1 and computer_choice == 2:
     print("YOU LOST!")
elif player_choice == 2 and computer_choice == 0:
    print("YOU LOST!")
elif player_choice == 0 and computer_choice == 2:
    print("YOU WON!")
elif player_choice == 1 and computer_choice == 0:
    print("YOU WON!")
elif player_choice == 2 and computer_choice == 1:
    print("YOU WON!")
else:
    print("Invalid Entry.")