from bicycles import Bike_Shop
from bicycles import Bicycle
from bicycles import Customer

if __name__ == '__main__':
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
    martha.buy(bike_shop, black_bicycle)
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
