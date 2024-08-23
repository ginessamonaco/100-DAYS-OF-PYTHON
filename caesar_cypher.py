alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            if shifted_position > 25:
                shifted_position2 = (alphabet.index(letter) - 25) + (shift_amount - 1)
                cipher_text += alphabet[shifted_position2]
            else:
                cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) - shift_amount
            if shifted_position < 0:
                shifted_position2 = (alphabet.index(letter) + 25) - (shift_amount - 1)
                cipher_text += alphabet[shifted_position2]
            else:
                cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


stop = False

while not stop:

    if direction == "encode":
        encrypt(original_text = text, shift_amount = shift)
    elif direction == "decode":
        decrypt(original_text = text, shift_amount = shift)
    else:
        print(f"Invalid entry. You typed '{direction}'.")


    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

    if run_again == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    elif run_again == "no":
        print("Goodbye.")
        stop = True
    else:
        print(f"Invalid entry. You typed '{run_again}'.")