operations = ["+", "-", "*", "/"]

def addition(x, y):
    result = x + y
    return result

def subtraction(x, y):
    result = x - y
    return result

def multiplication(x, y):
    result = x * y
    return result

def division(x, y):
    result = x / y
    return result

done_calculating = False

while not done_calculating:
    first_number = float(input("Enter a number: "))

    restart = False

    while not restart:
        valid = False

        while not valid:
            for o in operations:
                print(o)

            chosen_operation = input("Enter an operation: ")

            if chosen_operation not in operations:
                print("Invalid entry.")
            else:
                valid = True

        second_number = float(input("Enter another number: "))

        if chosen_operation == "+":
            output = addition(first_number, second_number)
            print(f"{first_number} + {second_number} = {output}")
        elif chosen_operation == "-":
            output = subtraction(first_number, second_number)
            print(f"{first_number} - {second_number} = {output}")
        elif chosen_operation == "*":
            output = multiplication(first_number, second_number)
            print(f"{first_number} * {second_number} = {output}")
        elif chosen_operation == "/":
            output = division(first_number, second_number)
            print(f"{first_number} / {second_number} = {output}")

        continue_restart = input(f"Type 'y' to continue calculating using {output}, 'n' to restart, or 'stop' to stop calculating:\n").lower()

        if continue_restart == "n":
            print("\n")
            restart = True
        elif continue_restart == "y":
            first_number = output
            print(f"First number: {first_number}")
        else:
            restart = True
            done_calculating = True

print(f"Calculation complete. {output} is the final number.")
