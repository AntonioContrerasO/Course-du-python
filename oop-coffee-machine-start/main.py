from platform import machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def machine():
    moneyM = MoneyMachine()
    coffeeM = CoffeeMaker()
    menu = Menu()
    while True:
        coffee = input("What would you like? (espresso/latte/cappuccino)")
        drink = menu.find_drink(coffee)
        if coffee == "report":
            coffeeM.report()
            moneyM.report()
        elif coffee == "off":
            break
        elif drink is not None:
            if coffeeM.is_resource_sufficient(drink) and moneyM.make_payment(drink.cost):
                coffeeM.make_coffee(drink)
        else:
            continue


machine()
