from bicycles import Bike_Shop
from bicycles import Bicycle
from bicycles import Wheels
from bicycles import Frame
from bicycles import Customer

if __name__ == '__main__':
    
    aluminum_wheels = Frame("aluminum", 20, 40)
    carbon_wheels = Frame("carbon", 50, 90)
    steel_wheels = Frame("steel", 100, 150)
    
    aluminum_frame = Frame("aluminum", 40, 50)
    carbon_frame = Frame("carbon", 60, 160)
    steel_frame = Frame("steel", 80, 320)
    
    
    red_bicycle = Bicycle("Red Bicycle", aluminum_wheels, aluminum_frame)
    blue_bicycle = Bicycle("Blue Bicycle", aluminum_wheels, carbon_frame)
    green_bicycle = Bicycle("Green Bicycle", carbon_wheels, carbon_frame)
    black_bicycle = Bicycle("Black Bicycle", steel_wheels, steel_frame)
    silver_bicycle = Bicycle("Silver Bicycle", steel_wheels, carbon_frame)
    gold_bicycle = Bicycle("Gold Bicycle", steel_wheels, steel_frame)
    
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
    print("")
    bike_shop.see_profits()
    print("")
    
    bike_shop.display_within_customer_funds(fred)
    print("")
    fred.buy(bike_shop, blue_bicycle)
    print("")
    bike_shop.display_inventory()
    print("")
    bike_shop.see_profits()
    print("")   
    
    bike_shop.display_within_customer_funds(martha)
    print("")
    martha.buy(bike_shop, green_bicycle)
    print("")
    bike_shop.display_inventory()
    print("")
    bike_shop.see_profits()
    print("")
    
    bike_shop.display_within_customer_funds(jack)
    print("")
    jack.buy(bike_shop, gold_bicycle)
    print("")
    bike_shop.display_inventory()
    print("")
    bike_shop.see_profits()
