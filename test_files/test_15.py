# coffee machine app
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
    "money": ["$", 0]
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
        if req[i] > resources[i]:
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
    


make_coffee("cappuccino")

# espresso = water: 50ml, coffee: 18g = price: $1.50
# latte = water: 200ml, coffee: 24g, milk: 150ml = price: $2.50
# cappuccino = water: 250ml, coffee: 24g, milk: 100ml = price: $3.00

# coin operated: accepts penny:$0.01, nickel:$0.05, dime:$0.10, quarter:$0.25

# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino)
choice = input("What would you like? (espresso/latte/cappuccino): ").lower()


# TODO: 2a. Turn off the Coffee Machine by entering “ off ” to the prompt.
machine_running = True
if choice == "off":
    machine_running = False


# TODO: 4. Process coins.

# TODO: 5. Check transaction successful.



