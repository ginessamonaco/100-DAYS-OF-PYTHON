import math

print("Welcome to the tip calculator!")

bill = input("What was the total bill?\n$")
tip_percent = input("How much tip would you like to give? 10, 15, or 20?\n")
people = input("How many people are splitting the bill?\n")

tip = (float(bill) * (float(tip_percent) * 0.01))
total = ((float(bill) + tip) / float(people))

total2 = round(total, 2)
total2 = "{:.2f}".format(total)

print(f"Each person should pay: ${total2}")
