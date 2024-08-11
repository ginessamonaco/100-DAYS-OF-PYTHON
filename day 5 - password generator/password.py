import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special = ["!", "@", "#", "$", "%", "^", "&", "*"]
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ABC = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

print("\nWelcome to the Password Generator.")

num_of_char = int(input("\nHow many characters do you want your password to have? Pick a between 1 and 20.\n"))
if (num_of_char > 20) or (num_of_char < 1):
    print("\nInvlalid Response. Start Over.\n")
else:
    num_of_numbers = int(input(f"\nHow many numbers do you want your password to have? Pick a number between 0 and {num_of_char}.\n"))
    if (num_of_numbers > num_of_char) or (num_of_numbers < 0):
        print("\nInvlalid Response. Start Over.\n")
    else:
        num_of_special = int(input(f"\nHow many special characters do you want your password to have? Pick a number between 0 and {num_of_char - num_of_numbers}.\n"))
        if (num_of_special > (num_of_char - num_of_numbers)) or (num_of_special < 0):
            print("\nInvlalid Response. Start Over.\n")
        else:
            num_of_letters = ((num_of_char - num_of_numbers) - num_of_special)
            num_of_abc = random.randint(0, num_of_letters)
            num_of_ABC = (num_of_letters - num_of_abc)
            password_char_list = list(range(1, num_of_char + 1))

            nums = (random.choices(numbers, k = num_of_numbers))
            specs = (random.choices(special, k = num_of_special))
            lowercase = (random.choices(abc, k = num_of_abc))
            uppercase = (random.choices(ABC, k = num_of_ABC))
            password_list = (nums + specs + lowercase + uppercase)
            random.shuffle(password_list)

            final_password = ""
            for word in password_list:
                final_password += word

            print("\nGenerating Password...")
            print(final_password + "\n")