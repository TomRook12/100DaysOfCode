drinks = {
    "Espresso":
        {"Water": 50,
         "Coffee": 18,
         "Milk": 0,
         "Cost": 1.5},

    "Latte":
        {"Water": 200,
         "Coffee": 24,
         "Milk": 150,
         "Cost": 2.5},

    "Cappuccino":
        {"Water": 250,
         "Coffee": 24,
         "Milk": 100,
         "Cost": 3}
    }

resources = {
    "Water": 300,
    "Coffee": 100,
    "Milk": 200,
    "Money": 0

    }

coins = {
    "Penny": 0.01,
    "Nickel": 0.5,
    "Dime": 0.1,
    "Quarter": 0.25
}

def coffee_resources(beverage):
    if resource_levels("Water", beverage) > 0:
        if resource_levels("Coffee", beverage) > 0:
            if resource_levels("Milk", beverage) > 0:
                resources["Water"] = resource_levels("Water", beverage)
                resources["Coffee"] = resource_levels("Coffee", beverage)
                resources["Milk"] = resource_levels("Milk", beverage)
            else:
                print("Not enough milk")
        else:
            print("Not enough coffee")
    else:
        print("Not enough water")


def resource_levels(ingredient, beverage):
    result = resources[ingredient] - drinks[beverage][ingredient]
    return result

def payment(beverage):
    coins_inserted = {
        "Penny": 0,
        "Nickel": 0,
        "Dime": 0,
        "Quarter": 0
    }
    total_cost = drinks[beverage]["Cost"]
    print("$", total_cost)
    coins_inserted["Penny"] = int(input("How many pennies? "))
    coins_inserted["Nickel"] = int(input("How many nickels? "))
    coins_inserted["Dime"] = int(input("How many dimes? "))
    coins_inserted["Quarter"] = int(input("How many quarters? "))
    total_input = sum(coins[k] * coins_inserted[k] for k in coins)
    print("You inserted $", total_input)
    if total_input - total_cost > 0:
        print("Your change is $", total_input - total_cost)
        resources["Money"] = resources["Money"] + total_cost
        return 1
    else:
        return 0

print(resources)

drink = ""

while drink != "off":
    drink = input("What drink would you like? (espresso/latte/cappucino) ")
    if drink == "resources":
        print(resources)
    elif drink == "off":
        print("Goodbye!")
    elif drink == "espresso":
        if payment("Espresso") == 1:
            coffee_resources("Espresso")
            print("Here is your espresso")
        else:
            print("You don't have enough money")
    elif drink == "latte":
        if payment("Latte") == 1:
            coffee_resources("Latte")
            print("Here is your latte")
        else:
            print("You don't have enough money")
    elif drink == "cappuccino":
        if payment("Cappuccino") == 1:
            coffee_resources("Cappuccino")
            print("Here is your cappuccino")
        else:
            print("You don't have enough money")
    else:
        print("We don't sell that beverage")

