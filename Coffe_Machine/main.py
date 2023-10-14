money = 0
profit = 0
coins = ["quarters", "dimes", "nickles", "pennies"]
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def show_resources(f_profit, product):
    profit = f_profit

    if product == "espresso" or product == "latte" or product == "cappuccino":
        resources["water"] -= MENU[product]["ingredients"]["water"]
        resources["milk"] -= MENU[product]["ingredients"]["milk"]
        resources["coffee"] -= MENU[product]["ingredients"]["coffee"]

    if product == "report":
        print(f"Water: {resources['water']} ml \nMilk: {resources['milk']} ml\nCoffee: {resources['coffee']} g \n"
              f"Money: ${profit}")


def check_resources(water, milk, coffee, product):
    if water < MENU[product]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif milk < MENU[product]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    elif coffee < MENU[product]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        return True


def process_coins():
    total = 0
    print("Please insert coins.")
    for i in coins:
        coin = float(input(f"How many {i}?: "))
        if i == "quarters":
            total = total+(coin * 0.25)
        elif i == "dimes":
            total = total+(coin * 0.10)
        elif i == "nickles":
            total = total+(coin * 0.05)
        elif i == "pennies":
            total = total+(coin * 0.01)
    return total


def check_enough_money(budget, product):
    f_profit = MENU[product]["cost"]
    change = (budget - MENU[product]["cost"])
    if budget == MENU[product]["cost"]:
        print(f"Here's your {product}. Enjoy!!!")
    elif budget > MENU[product]["cost"]:
        print(f"Here is ${round(change, 2)} dollars in change.")
        print(f"Here's your {product}. Enjoy!!!")
    elif budget < MENU[product]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    return f_profit


def deduction_of_resources(product):
    water = (resources["water"] - MENU[f"{product}"]["ingredients"]["water"])
    milk = (resources["milk"] - MENU[f"{product}"]["ingredients"]["milk"])
    coffee = (resources["coffee"] - MENU[f"{product}"]["ingredients"]["coffee"])

    return water, milk, coffee


""" ###############################          MAIN FUNCTION        ################################################# """


def coffe_program(f_profit):
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    match user_prompt:
        case "report":
            show_resources(f_profit, user_prompt)
            print("\n\n")
            coffe_program(f_profit)

        case "espresso":
            if check_resources(resources["water"], resources["milk"], resources["coffee"], user_prompt):
                money = process_coins()
                check_enough_money(money, user_prompt)
                f_profit += 1.5
                show_resources(f_profit, user_prompt)

            print("\n\n")
            coffe_program(f_profit)

        case "latte":
            if check_resources(resources["water"], resources["milk"], resources["coffee"], user_prompt):
                money = process_coins()
                check_enough_money(money, user_prompt)
                f_profit += 2.5
                show_resources(f_profit, user_prompt)

            print("\n\n")
            coffe_program(f_profit)

        case "cappuccino":
            if check_resources(resources["water"], resources["milk"], resources["coffee"], user_prompt):
                money = process_coins()
                check_enough_money(money, user_prompt)
                f_profit += 3.0
                show_resources(f_profit, user_prompt)

            print("\n\n")
            coffe_program(f_profit)

        case "off":
            print("Thanks for using the machine.")
            return


coffe_program(profit)
































