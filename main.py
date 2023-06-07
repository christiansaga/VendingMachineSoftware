from menu import Menu

menu = Menu()
# items and what they cost
ITEMS = {
    "Chips": {
        "Cost": 2.25
    },
    "Granola Bar": {
        "Cost": 1.25
    },
    "Chocolate Bar": {
        "Cost": 1.95
    },
    "Candy": {
        "Cost": 1.50
    },
    "Popcorn": {
        "Cost": 2.00
    }
}

# how much is available currently in the vending machine.
inventory_stock = {
    "Chips": 8,
    "Granola Bar": 7,
    "Chocolate Bar": 6,
    "Candy": 5,
    "Popcorn": 4,
}


def enough_snacks(inventory):
    """Checks to see if the snack has enough inventory to sell to the customer."""
    if inventory < 1:
        print("\n\n\nSorry that snack is out of stock.\nPlease make a different selection.\n\n\n")
        return False
    else:
        return True


def get_money():
    """Collects total amount of money the customer inserts into the vending machine"""
    print("Insert money.")
    total = int(input("dollars inserted?: ")) * 1.0
    total += int(input("quarters inserted?: ")) * 0.25
    total += int(input("dimes inserted?: ")) * 0.1
    total += int(input("nickles inserted?: ")) * 0.05
    total += int(input("pennies inserted?: ")) * 0.01
    return total


def enough_to_buy(funds_received, snack_cost):
    """checking if the amount of funds received from customer is greater than or equal to the cost of snack"""
    print(f"\n\n\nYou inserted ${funds_received:.2f}.")
    if funds_received >= snack_cost:
        change = round(funds_received - snack_cost, 2)
        print(f"${change} is your change.")
        return True
    else:
        print("\n\nYou did not insert enough money.\nTry again\n\n\n")
        return False


def deduct_inventory(amounts):
    """Deduct vending machine inventory"""
    inventory_stock[amounts] -= 1


functioning = True

while functioning:
    print("Welcome to Grand Mall Vending Machine.\n\nHere are your selections:\n")
    options = menu.get_items()
    print(options)
    decision = input("\n\nWhat would you like to order? \n\nor Type \"cancel\" to exit. \n").title()
    if decision == "Cancel":
        break
    if decision not in ITEMS:
        functioning = True
        print("\n\n\nThat is an invalid entry. Please try again.\n\n\n")

    else:
        supply = inventory_stock[decision]
        item = ITEMS[decision]
        if enough_snacks(supply):
            money_received = get_money()
            if enough_to_buy(money_received, item["Cost"]):
                deduct_inventory(decision)
            print(f"Here is your {decision}. Enjoy!\n\n\n")
