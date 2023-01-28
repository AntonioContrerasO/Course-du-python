MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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


def checker(coffee):
    if resources["water"] >= MENU[coffee]["ingredients"]["water"]:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        if coffee != "espresso":
            resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        return True
    else:
        return False


def change(coffee):
    print("Please insert coins.")
    quarters = int(input("how many quarters?")) * 0.25
    dimes = int(input("how many dimes?")) * 0.10
    nickles = int(input("how many nickles?")) * 0.05
    pennies = int(input("how many pennies?")) * 0.01
    total = quarters + dimes + nickles + pennies
    cambio = round(total - MENU[coffee]["cost"],2)
    if total >= 0:
        print(f"Here is {cambio} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def manchine():
    money = 0
    while True:
        coffee = input("What would you like? (espresso/latte/cappuccino)").lower()
        if coffee == "report":
            print(resources)
            print(f"Money: ${money}")
        elif coffee == "off":
            break
        else:
            if checker(coffee):
                if change(coffee):
                    money += MENU[coffee]["cost"]
                    print(f"Here is your {coffee} ☕️. Enjoy!")
            else:
                print("Sorry there is not enough water.")


manchine()
