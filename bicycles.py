class Bike_Shop():
    def __init__(self):
        self.name = "Good Bikes"
        self.inventory = {}
        self.profit = 0
        
    def sell(self, Bicycle):
        self.inventory[Bicycle] = self.inventory[Bicycle] - 1
        self.profit = Bicycle.cost_to_produce + Bicycle.cost_to_produce * .2
    
    def display_inventory(self):
        for i in self.inventory:
            print("Bike Model: {0} + Price: {1}").format(i.name, self.inventory[i])
    
    def see_profits(self):
        print(self.profit)
    
    def display_within_customer_funds(self, Customer):
        print("Bicycles that you can afford")
        for i in self.inventory:
            if Customer.funds > i.cost_to_produce:
                print("Model: {0} + Price: {1}").format(i.name, (i.cost_to_produce + i.cost_to_produce * .2))
    
class Bicycle():
    def __init__(self, name, weight, cost_to_produce):
        self.name = name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

class Customer():
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.my_bicycle = None
    
    def buy(self, Bicycle):
        self.my_bicycle = Bicycle

red_bicycle = Bicycle("Red Bicycle", 100, 60)
blue_bicycle = Bicycle("Blue Bicycle", 110, 140)
green_bicycle = Bicycle("Green Bicycle", 120, 210)
black_bicycle = Bicycle("Black Bicycle", 130, 400)
silver_bicycle = Bicycle("Silver Bicycle", 140, 620)
gold_bicycle = Bicycle("Gold Bicycle", 150, 800)

bike_shop = Bike_Shop()
bike_shop.inventory[red_bicycle] = 6
bike_shop.inventory[blue_bicycle] = 8
bike_shop.inventory[green_bicycle] = 4
bike_shop.inventory[black_bicycle] = 5
bike_shop.inventory[silver_bicycle] = 3
bike_shop.inventory[gold_bicycle] = 2

fred = Customer("Fred", 200)
martha = Customer("Martha", 500)
jack = Customer("Jack", 1000)

bike_shop.display_inventory()
bike_shop.sell(red_bicycle)
print("")
bike_shop.display_inventory()
bike_shop.see_profits()

bike_shop.display_within_customer_funds(fred)

fred.buy(red_bicycle)
print(fred.my_bicycle.name)