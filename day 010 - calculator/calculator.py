import operator

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

def calculate():
    start_over = False
    first_num = float(input("Enter the first number: "))

    while not start_over:
        for key in operations:
            print(key)

        chosen_operation = input("Enter an operation: ")
        second_num = float(input("Enter the next number: "))

        if chosen_operation == "+":
            last_num = first_num + second_num
        elif chosen_operation == "-":
            last_num = first_num - second_num
        elif chosen_operation == "*":
            last_num = first_num * second_num
        elif chosen_operation == "/":
            last_num = first_num / second_num

        print(f"{first_num} {chosen_operation} {second_num} = {last_num}")
        continue_or_new = input(f"Type 'yes' to continue with the number {last_num}, type 'no' to start a new calculation:\n")

        if continue_or_new == "no":
            start_over = True
        else:
            first_num = last_num
            print(f"Starting number: {first_num}")

repeat = True

while repeat:
    calculate()
