import pandas

names = pandas.read_csv("nato_phonetic_alphabet.csv")
names_dict = {row.letter: row.code for (index, row) in names.iterrows()}

is_on = True
while is_on:
    try:
        user_name = input("Type your name. ").upper()
        coded_name = [names_dict[f"{char}"] for char in user_name]
        print(coded_name)
        is_on = False
    except KeyError:
        print("Sorry, only letters please.")
