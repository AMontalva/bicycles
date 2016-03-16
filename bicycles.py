class Bicycle_Manufacturer():
    def __init__(self, name):
        self.name = name
        self.bicycle_models = {}
        self.profit = 0
    
    def build_bicycle(self, Bicycle):
        self.bicycle_models[Bicycle.name] = Bicycle
        Bicycle.manufacturer = self.name

    def sell(self, Bicycle):
        self.profit = self.profit + Bicycle.cost_to_produce + Bicycle.cost_to_produce * .2

class Bicycle_Shop():
    def __init__(self):
        self.name = "Good Bikes"
        self.inventory = {}
        self.profit = 0
        
    def buy_from_manufacturer(self, Bicycle_Manufacturer, Bicycle, ammount):
        if(Bicycle.name in Bicycle_Manufacturer.bicycle_models):
            self.inventory[Bicycle] = ammount
            Bicycle.cost_to_produce = Bicycle.cost_to_produce + (Bicycle.cost_to_produce * .2)
            for i in range(ammount):
                Bicycle_Manufacturer.sell(Bicycle)
        else:
            print("{0} does not manufacture {1}".format(Bicycle_Manufacturer.name, Bicycle.name))
            
        
    def sell(self, Bicycle):
        self.inventory[Bicycle] = self.inventory[Bicycle] - 1
        self.profit = self.profit + Bicycle.cost_to_produce + Bicycle.cost_to_produce * .2
    
    def display_inventory(self):
        for i in self.inventory:
            print("Bicycle Model: {0} + Inventory: {1}".format(i.name, self.inventory[i]))
    
    def see_profits(self):
        print("{0} profits are {1:.2f}".format(self.name, self.profit))
    
    def display_within_customer_funds(self, Customer):
        print("Bicycles that you can afford")
        for i in self.inventory:
            if Customer.funds >= i.cost_to_produce:
                print("Model: {0} + Price: {1:.2f}".format(i.name, (i.cost_to_produce + i.cost_to_produce * .2)))
    
class Bicycle():
    def __init__(self, name, Wheels, Frame):
        self.name = name
        self.weight = Frame.weight + (Wheels.weight * 2)
        self.cost_to_produce = Frame.cost_to_produce + (Wheels.cost_to_produce * 2)
        self.manufacturer = ""
        
class Wheels():
    def __init__(self, name, weight, cost_to_produce):
        self.name = name
        self.weight = weight
        self.cost_to_produce = cost_to_produce

class Frame():
    def __init__(self, type, weight, cost_to_produce):
        self.type = type
        self.weight = weight
        self.cost_to_produce = cost_to_produce

class Customer():
    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.my_bicycle = None
    
    def buy(self, Bicycle_Shop, Bicycle):
        if self.funds >= Bicycle.cost_to_produce + Bicycle.cost_to_produce * .2:
            Bicycle_Shop.sell(Bicycle)
            self.my_bicycle = Bicycle
            print("{0} owns a brand new {1}".format(self.name, self.my_bicycle.name))
            self.funds = self.funds - (Bicycle.cost_to_produce + Bicycle.cost_to_produce * .2)
            print("Spent {0:.2f}, currently have {1:.2f} left in your funds".format(Bicycle.cost_to_produce + Bicycle.cost_to_produce * .2, self.funds))
        else:
            print("Can't afford this bicycle")

