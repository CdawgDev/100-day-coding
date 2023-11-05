from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
menu_item = MenuItem
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# available_coffee = coffee_menu.get_items()

machine_running = True

def get_user_selection():
    available_coffee = coffee_menu.get_items()
    choice = input(f"What would you like? {available_coffee}:")
    return choice

def print_machine_report():
    coffee_maker.report()
    money_machine.report()


while machine_running:
    choice = get_user_selection().lower()
    drink = coffee_menu.find_drink(choice)
    if choice == "off":
        print("Machine Powering Off!")
        machine_running = False
    elif choice == "report":
        print_machine_report()
    if drink != None:
        enough_resources = coffee_maker.is_resource_sufficient(drink)
        if enough_resources:
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)