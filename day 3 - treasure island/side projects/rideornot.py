print("Welcome to the ride!")
name = input("What is your name?\n")

print("HI " + name.upper() + "!")
age = int(input("How old are you?\n"))

if age < 12:
    print("Sorry, are not old enough to ride.")
elif 12 < age < 18:
    height = int(input("How tall are you in inches?\n"))
    if height >= 60:
        print("You are allowed to ride!")
    else: 
        print("Sorry, you are not tall enough to ride.")
elif age >= 18:
    height = int(input("How tall are you in inches?\n"))
    if height >= 60:
        print("You are allowed to ride!")
    else:
        print("Sorry, you are not tall enough to ride.")
else:
    print("You are allowed to ride!")