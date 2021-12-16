# coffee machine app

# Setup code
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
    "water": [300, "ml"],
    "milk": [200, "ml"],
    "coffee": [100, "g"],
    "money": ["$", 0],
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

# Functions
# TODO: 2b. Print report function.


def print_report():
    """loops through all resources dictionary and prints current contents"""
    for i in resources:
        print(f"{i}: {resources[i][0]}{resources[i][1]}")

# TODO: 3. Check resources sufficient


def check_resources(req):
    """Takes req as a dictionary and checks against available resources"""
    for i in resources:
        if req[i] > resources[i][0]:
            return False
        else:
            return True

# TODO: 6. Make Coffee.


def make_coffee(coffee):
    """take input as entry in menu dictionary, reduce resources by amount in the menu"""
    resources["water"][0] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"][0] -= MENU[coffee]["ingredients"]["coffee"]
    resources["money"][1] += MENU[coffee]["cost"]
    if "milk" in MENU[coffee]["ingredients"]:
        resources["milk"][0] -= MENU[coffee]["ingredients"]["milk"]

# TODO: 4. Process coins.


def process_coins():
    total = 0
    for n in coins:
        amount = int(input(f"how many {n}?:"))
        total += amount * coins[n]
    return round(total, 2)

# TODO: 5. Check transaction successful.


def check_success(req):
    given = process_coins()
    if req == given:
        return True
    elif req < given:
        print(f"Here is ${given - req} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino)
machine_running = True

while machine_running:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice in MENU:
        if check_resources(MENU[choice]["ingredients"]):
            if check_success(MENU[choice]["cost"]):
                make_coffee(choice)
        else:
            print("Sorry there is not enough water")
    elif choice == "report":
        print_report()
    # TODO: 2a. Turn off the Coffee Machine by entering “ off ” to the prompt.
    elif choice == "off":
        machine_running = False
    else:
        print("Not an option")











