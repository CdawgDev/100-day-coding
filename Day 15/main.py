#Make 3 hot flavors

# Espresso, Latte, Cappuccino

# Espresso 50ml Water, 18 coffee $1.50
# Latte 200ml Water 24g coffee 150ml Milk $.
# Cappuccino 250ml water, 24g coffee, 100ml Milk

from coffee_data import MENU
from coffee_data import resources as machine_data


def print_report(coffee_resources):
    """Prints the Current amount of resources available in the machine"""
    print(f'Water: {coffee_resources["water"]}ml')
    print(f'Milk: {coffee_resources["milk"]}ml')
    print(f'Coffee: {coffee_resources["coffee"]}g')
    print(f'Money: ${coffee_resources["money"]}')

def check_resources(type_coffee, coffee_resources):
    """Takes in type of coffee and the amount of resources in the machine. Returns either T/F or the item that is missing."""
    if type_coffee not in MENU:
        print("Sorry We don't sell that here")
        return False
    coffee_ingredients = MENU[f"{type_coffee}"]["ingredients"]
    count = 0
    missing_resources = ""
    for x in coffee_ingredients:
        if coffee_resources[x] > coffee_ingredients[x]:
            count += 1
        else:
            missing_resources = x
    if len(coffee_ingredients) == count:
        coffee_price = MENU[type_coffee]["cost"]
        print(f"The price of ${type_coffee} {coffee_price}")
        return True
    else:
        return missing_resources

def update_machine(coffee,current_resources):
    """Takes the coffee selected and current resources in the machine. Returns the new list resources in the machine"""
    resources_used = MENU[f"{coffee}"]["ingredients"]
    amount = MENU[f"{coffee}"]["cost"]
    updated_resources = current_resources
    current_resources["money"] += amount
    for x in resources_used:
        updated_resources[f"{x}"] -= resources_used[x]
    return updated_resources

def check_payment(type_of_coffee):
    """Takes in the type of coffee and asks the user for 4 inputs of coins. Returns True or False"""
    cost_of_coffee = MENU[f"{type_of_coffee}"]["cost"]
    print("Please Insert coins.")
    quarters  = float(input("How many quarters ?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.10
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    coins_collected = quarters  + dimes + nickles + pennies
    if coins_collected >= cost_of_coffee:
        change = coins_collected - cost_of_coffee
        print(f"Here is ${round(change,2)} in change.")
        print(f"Here is your {type_of_coffee}. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def run_machine():
    resources = machine_data
    resources["money"] = 0
    machine_running = True
    while machine_running:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "report":
            print_report(resources)
        elif user_input == "exit":
            print("Thank you for using cory's coffee machine")
            return
        else:
            check_machine_resources = check_resources(user_input, resources)
            if check_machine_resources == True:
                payment = check_payment(user_input)
                if payment:
                    resources = update_machine(user_input,resources)
            else:
                print(f"Sorry we don't have enough {check_machine_resources}")

run_machine()