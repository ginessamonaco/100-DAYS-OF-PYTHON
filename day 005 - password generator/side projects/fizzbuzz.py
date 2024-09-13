# target = int(input("Pick a number between 15 and 100:/n"))

# for number in range(1, target + 1):
#     num = ""
#     if number % 3 == 0:
#         num = "Fizz"
#     if number % 5 == 0:
#         num = "Buzz"
#     if number % 3 == 0 and number % 5 == 0:
#         num = "FizzBuzz"
#     if number % 3 != 0 and number % 5 != 0:
#         num = str(number)
#     print(num)

for number in range(1, 101):
    num = ""
    if number % 3 == 0:
        num = "Fizz"
    if number % 5 == 0:
        num = "Buzz"
    if number % 15 == 0:
        num = "FizzBuzz"
    if (number % 3 != 0) and (number % 5 != 0):
        num = str(number)
    print(num)