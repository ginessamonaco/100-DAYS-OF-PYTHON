print("Customize your pizza :D")
size = input('Small "S"/ Medium "M"/ Large "L":\n')
pepperoni = input('Pepperoni "Y"/ No "N":\n')
extra_cheese = input('Extra Cheese "Y"/ No "N":\n')

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill += 0

if extra_cheese == "Y":
    bill += 1
else:
    bill += 0

print("Calculating your total...")
print(f"Your total is: ${bill}.")
