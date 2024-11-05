import pandas as pd

nato_content = pd.read_csv("nato_phonetic_alphabet.csv")

user_word = input("Enter a word: ").upper()

nato_dict = {row.letter:row.code for (index, row) in nato_content.iterrows()}

phonetic_code_list = [nato_dict[letter] for letter in user_word]
print(phonetic_code_list)