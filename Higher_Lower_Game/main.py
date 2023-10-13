from game_data import data
from art import vs
from art import logo
import random


# The function generates de option A
def option_a():
    a = random.choice(data)
    a_followers = f'{a["follower_count"]}'
    a = f'{a["name"]}, {a["description"]}, {a["country"]}'
    print(a)

    return a_followers, a


# The function generates de option B
def option_b():
    print(vs)
    b = random.choice(data)
    b_followers = f'{b["follower_count"]}'
    b = f'{b["name"]}, {b["description"]}, {b["country"]}'
    print(b)

    return b_followers, b


# This function converts the option B to the option A. So if the user guess right. Option B pass to be the option A.
def turning_b_to_a(followers, name):
    b_followers = followers
    print(name)

    return b_followers


game_over = True
function_score = 0
# Generates the first option A
answer_a = option_a()

while game_over:
    answer_b = option_b()
    user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Makes sure that option A and Option B are not the same
    if answer_a == answer_b:
        answer_b = option_b()

    # Defines rather option A is bigger than option B. Or vice-versa
    if int(answer_a[0]) > int(answer_b[0]):
        answer = "A"
        print(f"A is bigger. \nA has {answer_a[0]} and B has {answer_b[0]} \n\n")
    else:
        answer = "B"
        print(f"B is bigger. \nB has {answer_b[0]} and A has {answer_a[0]} \n\n")

    # Defines if the answer of the user is right or not
    if user_answer != answer:
        game_over = False
        print(f"Sorry, that's wrong. Final score: {function_score}")

    if user_answer == answer:
        function_score += 1
        print(f"You're right!!! Your score is: {function_score}")
        answer_a = turning_b_to_a(answer_b, answer_b[1])


