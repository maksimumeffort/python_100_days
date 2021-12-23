from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
register = MoneyMachine()
coffee_machine = CoffeeMaker()

# options available
options = {
    "espresso": menu.find_drink("espresso"),
    "latte": menu.find_drink("latte"),
    "cappuccino": menu.find_drink("cappuccino")
}

machine_running = True

while machine_running:

    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice in options:
        drink = menu.find_drink(choice)
        # TODO: 4. check transaction success
        if coffee_machine.is_resource_sufficient(drink):
            # TODO: 3. process coins
            if register.make_payment(drink.cost):
                # TODO: 5. make coffee
                coffee_machine.make_coffee(drink)
    elif choice == "report":
        # TODO: 1. print report
        coffee_machine.report()
        register.report()
    elif choice == "off":
        machine_running = False
    else:
        print("Not an option")
