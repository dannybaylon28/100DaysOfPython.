import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
signs = [rock, paper, scissors]

user_choice = signs[int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))]
cpu_choice = signs[random.randint(0,2)]

print(user_choice)
print(cpu_choice)


if user_choice == rock:

    if cpu_choice == rock:
        print("TIE!!!")
    elif cpu_choice == paper:
        print("CPU WINS!!!")
    elif cpu_choice == scissors:
        print("USER WINS!!!")


if user_choice == paper:

    if cpu_choice == rock:
        print("USER WINS!!!")
    elif cpu_choice == paper:
        print("TIE!!!")
    elif cpu_choice == scissors:
        print("CPU WINS!!!")

if user_choice == scissors:

    if cpu_choice == rock:
        print("CPU WINS!!!")
    elif cpu_choice == paper:
        print("USER WINS!!!")
    elif cpu_choice == scissors:
        print("TIE!!!")