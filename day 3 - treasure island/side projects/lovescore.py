print("")




name1 = input("What is your name?\n")
name2 = input("Hi " + name1 + ". What is your partner's name?\n")

t = name1.lower().count("t") + name2.lower().count("t")
r = name1.lower().count("r") + name2.lower().count("r")
u = name1.lower().count("u") + name2.lower().count("u")
e = name1.lower().count("e") + name2.lower().count("e")
l = name1.lower().count("l") + name2.lower().count("l")
o = name1.lower().count("o") + name2.lower().count("o")
v = name1.lower().count("v") + name2.lower().count("v")
e = name1.lower().count("e") + name2.lower().count("e")

true = t + r + u + e
love = l + o + v + e

number = int(str(true) + str(love))

if number  < 10:
    print(f"Your love score is {number}. You don't belong together.")
elif number < 25:
    print(f"Your love score is {number}. That isn't too good.")
elif number < 50:
    print(f"Your love score is {number}. Not too shabby.")
elif number < 70:
    print(f"Your love score is {number}. You must really like each other.")
elif number < 85:
    print(f"Your love score is {number}. Awww... such a great couple.")
elif number < 95:
    print(f"Your love score is {number}. Ya'll are great together.")
elif number < 100:
    print(f"Your love score is {number}. You are perfect together.")
else:
    print(f"Your love score is {number}. How?")