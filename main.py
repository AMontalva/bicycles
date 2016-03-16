from bicycles import Frame, Wheels, Customer, Bicycle, Bicycle_Shop, Bicycle_Manufacturer

if __name__ == '__main__':
    
    aluminum_wheels = Frame("aluminum", 20, 40)
    carbon_wheels = Frame("carbon", 50, 90)
    steel_wheels = Frame("steel", 100, 150)
    
    aluminum_frame = Frame("aluminum", 40, 50)
    carbon_frame = Frame("carbon", 60, 120)
    steel_frame = Frame("steel", 80, 320)
    
    
    red_bicycle = Bicycle("Red Bicycle", aluminum_wheels, aluminum_frame)
    blue_bicycle = Bicycle("Blue Bicycle", aluminum_wheels, carbon_frame)
    green_bicycle = Bicycle("Green Bicycle", carbon_wheels, carbon_frame)
    black_bicycle = Bicycle("Black Bicycle", steel_wheels, carbon_frame)
    silver_bicycle = Bicycle("Silver Bicycle", carbon_wheels, steel_frame)
    gold_bicycle = Bicycle("Gold Bicycle", steel_wheels, steel_frame)

    cool_bicycles_manufacturers = Bicycle_Manufacturer("Cool Bicycles Manufacturer")
    cool_bicycles_manufacturers.build_bicycle(red_bicycle)
    cool_bicycles_manufacturers.build_bicycle(blue_bicycle)
    cool_bicycles_manufacturers.build_bicycle(green_bicycle)
    
    hot_bicycles_manufacturers = Bicycle_Manufacturer("Hot Bicycles Manufacturer")
    hot_bicycles_manufacturers.build_bicycle(black_bicycle)
    hot_bicycles_manufacturers.build_bicycle(silver_bicycle)
    hot_bicycles_manufacturers.build_bicycle(gold_bicycle)
    
    bicycle_shop = Bicycle_Shop()
    bicycle_shop.buy_from_manufacturer(cool_bicycles_manufacturers, red_bicycle, 6)
    bicycle_shop.buy_from_manufacturer(cool_bicycles_manufacturers, blue_bicycle, 8)
    bicycle_shop.buy_from_manufacturer(cool_bicycles_manufacturers, green_bicycle, 4)
    bicycle_shop.buy_from_manufacturer(hot_bicycles_manufacturers, black_bicycle, 5)
    bicycle_shop.buy_from_manufacturer(hot_bicycles_manufacturers, silver_bicycle, 3)
    bicycle_shop.buy_from_manufacturer(hot_bicycles_manufacturers, gold_bicycle, 2)
    
    print("")
    
    fred = Customer("Fred", 200)
    martha = Customer("Martha", 500)
    jack = Customer("Jack", 1000)
    
    bicycle_shop.display_inventory()
    print("")
    bicycle_shop.see_profits()
    print("")
    
    bicycle_shop.display_within_customer_funds(fred)
    print("")
    fred.buy(bicycle_shop, red_bicycle)
    print("")
    bicycle_shop.display_inventory()
    print("")
    bicycle_shop.see_profits()
    print("")   
    
    bicycle_shop.display_within_customer_funds(martha)
    print("")
    martha.buy(bicycle_shop, green_bicycle)
    print("")
    bicycle_shop.display_inventory()
    print("")
    bicycle_shop.see_profits()
    print("")
    
    bicycle_shop.display_within_customer_funds(jack)
    print("")
    jack.buy(bicycle_shop, gold_bicycle)
    print("")
    bicycle_shop.display_inventory()
    print("")
    bicycle_shop.see_profits()
