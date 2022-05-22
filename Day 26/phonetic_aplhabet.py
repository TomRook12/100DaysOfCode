import pandas

#{new_key:new_value for (index, row) in df.itteros()}

#Todo 1. Create a dictionary from the csv key = "A", value = Alfa

phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in phonetic_alphabet.iterrows()}

print(phonetic_dict)

#Todo 2. Create a list of phonetic code wwords from a wword that the user inputs

name = input("What's your name matey?").upper()
name_letters = list(name)
print(name_letters)

output_list = [phonetic_dict[letter] for letter in name_letters]
print(output_list)


