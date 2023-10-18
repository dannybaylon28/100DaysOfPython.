import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def report():
    coffee_maker.report()
    money_machine.report()


def check_if_drink_exists(drink):
    drink_exists = menu.find_drink(drink)
    return drink_exists


def check_resources(drink):
    if check_if_drink_exists(drink):
        resources = coffee_maker.is_resource_sufficient(menu.find_drink(drink))
        if not resources:
            return False
        return True


def process_coins(drink):
    if drink == "latte":
        cost = 2.5
    elif drink == "espresso":
        cost = 1.5
    elif drink == "cappuccino":
        cost = 3
    return money_machine.make_payment(cost)


def machine():
    while machine_on:
        drink = input(f"Choose your drink {menu.get_items()}? ")

        if drink == "report":
            report()
        elif drink == "off":
            return
        else:
            sufficient = check_resources(drink)
            if sufficient:
                money = process_coins(drink)
                if money:
                    coffee_maker.make_coffee(menu.find_drink(drink))


machine()








































