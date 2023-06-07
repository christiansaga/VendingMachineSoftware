class Items:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Menu:
    """a class for a vending machine menu. More items can be added if a vending machine company decides to do so."""

    def __init__(self):
        self.menu = {
            Items(name="Chips - $2.25", cost=2.25),
            Items(name="Granola Bar - $1.25", cost=1.25),
            Items(name="Chocolate Bar - $1.95", cost=1.95),
            Items(name="Candy - $1.50", cost=1.50),
            Items(name="Popcorn - $2.00", cost=2.00)
        }

    def get_items(self):
        """Loops all items and prices to customer."""
        options = ""
        for item in self.menu:
            options += (f"\n{item.name}")
        return options

