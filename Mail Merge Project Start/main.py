
# Bring the starting letter.
with open("C:/Users/Danie/OneDrive/Escritorio/GitHub/100DaysOfPython/Mail Merge Project Start/Input/Letters/"
          "starting_letter.txt", "r") as file:
    start = file.read()

# Saves the name list in the variable names
f = open("C:/Users/Danie/OneDrive/Escritorio/GitHub/100DaysOfPython/Mail Merge Project Start/Input/Names"
         "/invited_names.txt", "r")
names = f.readlines()

for name in names:
    # Eliminates the blank spaces in the word.
    new_name = name.strip()
    # Replace the [name] placeholder with the actual name.
    new_start = start.replace('[name]', new_name)
    # Creates the letter for each person.
    with open(f"C:/Users/Danie/OneDrive/Escritorio/GitHub/100DaysOfPython/Mail Merge Project Start/Output/ReadyToSend"
              f"/letter_for_{new_name}", "a") as file:
        file.write(new_start)





