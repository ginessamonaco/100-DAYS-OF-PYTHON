# ESCAPE ROOM - TRY NOT TO DIE
print("\nWelcome to the escape room!")
print("Your mission is to, well, ESCAPE!!!")

print("\nYou wake up and the last thing you remember is being told to escape. You stand up and look around.")
which_way = input("You're at a cross road. Where do you want to go? " + 'Type "left" or "right"\n')
if which_way == "left":
    pond = input("You've arrived at a pond. " + 'Type "boat" to wait for a boat. Type "swim" to swim across.\n')
    if pond == "boat":
        doors = input("You've stumbled upon three doors. " + 'Type "one", "two", or "three" to pick a door to walk through.\n')
        if (doors == "one") or (doors == "three"):
            rope_ladder = input("You walk through the door and are faced with a polar bear!!! " + 'Type "rope" to climb the rope. Type "ladder" to climb the ladder.\n')
            if rope_ladder == "rope":
                print("You run to the rope and climb it to escape the polar bear. At the top of the rope is a hole that leads you to the roof.")
                roof = input('Type "helicopter" to get onto the helicopter. Type "jump" to jump into the abyss below.\n')
                if roof == "jump":
                    print("You jump into the abyss and a net breaks your fall. You managed to escape without a scratch.")
                    money = input('Pick a hand, type "left" or "right", to discover how much money you have won!\n')
                    if money == "left":
                        print("You have won...")
                        print("NOTHING!!! Atleast you are alive though! :D")
                    else:
                        print("You have won...")
                        print("ONE BILLION MONIES!!! So nice!")
                        print("Bye now! :D")
                else:
                    print("You get onto the helicopter and it takes off. Moments later the engine begins to fail and the helicopter plummets to the ground!!!")
                    print("Unfortunately, nobody survived the crash. You are dead.")
            else:
                print("You start climbing the ladder when the bolts come loose. The ladder collapses and the bear runs up to you!!!")
                print("Long story short (aka the polar bear mauls you), you are dead.")
        else:
            print("You walk through the door and are faced with a man. He throws rocks at you!!!")
            print("The rocks smack you one by one!")
            print("You collapse and die.")
    else:
        print("You start swimming across when a snapping turtle swims up to you and bites a hole in your neck!!!")
        print("You are now dead.")
else:
    print("You turn right and get hit by a car!!!")
    print("You are dead! RIP.")
