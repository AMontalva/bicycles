class Bike_Shop():
    def __init__(self):
        self.name = "Good Bikes"
        self.inventory = {}
        self.profit = 0
        
    def sell(self, Bicycle):
        self.inventory[Bicycle] = self.inventory[Bicycle] - 1
        self.profit = self.profit + Bicycle.cost_to_produce + Bicycle.cost_to_produce * .2
    
    def display_inventory(self):
        for i in self.inventory:
            print("Bike Model: {0} + Price: {1}").format(i.name, self.inventory[i])
    
    def see_profits(self):
        print("{0} profits are {1}".format(self.name, self.profit))
    
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
    
    def buy(self, Bike_Shop, Bicycle):
        if self.funds > Bicycle.cost_to_produce + Bicycle.cost_to_produce * .2:
            Bike_Shop.sell(Bicycle)
            self.my_bicycle = Bicycle
            print("{0} owns a brand new {1}".format(self.name, self.my_bicycle.name))
            self.funds = self.funds - Bicycle.cost_to_produce + Bicycle.cost_to_produce * .2
            print("Spent {0}, currently have {1} left in your funds".format(Bicycle.cost_to_produce + Bicycle.cost_to_produce * .2, self.funds))
        else:
            print("Can't afford this bicycle")
