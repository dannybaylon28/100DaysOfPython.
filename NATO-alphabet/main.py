import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
names = pandas.read_csv("nato_phonetic_alphabet.csv")
names_dict = {row.letter: row.code for (index, row) in names.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("Type your name. ").upper()
coded_name = [names_dict[f"{char}"] for char in user_name]
print(coded_name)


