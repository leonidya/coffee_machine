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


# TODO: 4. Check transaction successful


def check_transaction(choice):
    quarters = int(input("how many quarters")) * 0.25
    dimes = int(input("how many dimes")) * 0.10
    nickles = int(input("how many nickles")) * 0.05
    pennies = int(input("how many pennies")) * 0.01
    sum = quarters + dimes + nickles + pennies
    if sum > MENU[choice]["cost"]:
        change = sum - MENU[choice]["cost"]
        change = (round(change,2))
        print(f"Here is {change} in change")
        print(f"here is your {choice}")
        make_coffee(choice)
        return MENU[choice]["cost"]
    elif sum == MENU[choice]["cost"]:
        print(f"here is your {choice}")
        make_coffee(choice)
        return MENU[choice]["cost"]
    else:
        print("Sorry that's not enough money")


# TODO: 3. CHECK RESOURCES
def check_resources(choice):
    for coffee in MENU:
        if choice == coffee and coffee == "espresso":
            if resources["water"] - MENU[coffee]["ingredients"]["water"] < 0:
                return print("Sorry there is no enough water")
            elif resources["coffee"] - MENU[coffee]["ingredients"]["coffee"] < 0:
                return print("Sorry there is no enough coffee")
            else:
                money1 = check_transaction(choice)
                return money1
        elif choice == coffee:
            if resources["water"] - MENU[coffee]["ingredients"]["water"] < 0:
                return print("Sorry there is no enough water")
            elif resources["coffee"] - MENU[coffee]["ingredients"]["coffee"] < 0:
                return print("Sorry there is no enough coffee")
            elif resources["milk"] - MENU[coffee]["ingredients"]["milk"] < 0:
                return print("Sorry there is no enough milk")
            else:
                money1 = check_transaction(choice)
                return money1

# TODO: 2. Make a Coffee ( check if there is sufficient resource and if input = report, print report.)

def make_coffee(choice):
    for coffee in MENU:
        if choice == coffee and coffee == "espresso":
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
            print(resources)
        elif choice == coffee:
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
            resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
            print(resources)


# TODO: 1. PROMPT USER BY ASKING "WHAD WOULD YOU LIKE?" (ESPRESSO/LATTE/CAPPUCCINO) - while loop
money2 = 0
out_of_work = False
while not out_of_work:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice == "off":
        out_of_work = True
    elif choice == "report":
        water = resources["water"]
        coffee = resources["coffee"]
        milk = resources["milk"]
        print(f"Report: Water: {water}, Milk: {milk}, Coffee: {coffee}, Money {money2}")
    else:
        money2 += check_resources(choice)
