class Bike_Shop():
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        
    def sell(self, Bicycle):
        self.inventory[Bicycle] = Bicycle
    
    def display_inventory(self):
        for i in self.inventory:
            print("Bike Model: {0} + Price: {1}").format(i.name, self.inventory[i])
    
class Bicycle():
    def __init__(self, name, weight, cost_to_produce):
        self.name = name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

class Customers():
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
    
    def buy(self):
        pass
        
    
red_bicycle = Bicycle("Red Bicycle", 100, 60)
blue_bicycle = Bicycle("Blue Bicycle", 200, 140)
green_bicycle = Bicycle("Green Bicycle", 300, 210)
black_bicycle = Bicycle("Black Bicycle", 500, 400)
silver_bicycle = Bicycle("Silver Bicycle", 800, 620)
gold_bicycle = Bicycle("Gold Bicycle", 1000, 800)

bike_shop = Bike_Shop("Good Bikes")
bike_shop.inventory[red_bicycle] = 6
bike_shop.inventory[blue_bicycle] = 8
bike_shop.inventory[green_bicycle] = 4
bike_shop.inventory[black_bicycle] = 5
bike_shop.inventory[silver_bicycle] = 3
bike_shop.inventory[gold_bicycle] = 2

bike_shop.display_inventory()