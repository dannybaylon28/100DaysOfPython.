import random

number = random.randint(1, 101)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "easy":
    attempts = 10
else:
    attempts = 5

game_over = True
while game_over:
    attempts -= 1
    guess_number = int(input("Make a guess: "))

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        game_over = False
    elif number == guess_number:
        print(f"You got it! The answer was {number}")
        game_over = False
    elif guess_number > number:
        print("Too high. \nTry Again")
        print(f"You have {attempts} attempts remaining to guess the number.\n\n")
    elif guess_number < number:
        print("Too Low. \nTry Again")
        print(f"You have {attempts} attempts remaining to guess the number. \n\n")




















































