from recipe import menu ,resources

def coin_process(coffee_type,money):
    """ It will take coffe type and total money as input, return the change,
    it will also check money is enough or not """
    
    if menu[coffee_type]["cost"]<=money:
        change= money- menu[coffee_type]["cost"]
        if change>0:
             return int(change)
        elif change==0:    
             return 0
        else:
            return "no"
    else:
        return "no"     
        
def coin_input():
    """ It will calculate total money """
    
    print("please insert your coins")
    r20 = int(input("how many 20 rupees coins: "))
    r10 = int(input("how many 10 rupees coins: "))
    r5  = int(input("how many 5 rupees coins: "))
   
    total = 20*r20 + 10*r10 + 5*r5 
    return int(total)

def resource_enough(coffee):
    """It will check , resources are enough or not to process the order """
    
    if coffee=="espresso":
        if menu[coffee]["ingredients"]["water"]<=resources["water"] and menu[coffee]["ingredients"]["coffee"]<=resources["coffee"]:
            return True
        else:
            return False
    else:
        if menu[coffee]["ingredients"]["water"]<=resources["water"] and menu[coffee]["ingredients"]["coffee"]<=resources["coffee"] and  menu[coffee]["ingredients"]["milk"]<=resources["milk"]:
            return True
        else:
            return False


def resources_check(coffee):
    """It will print all insufficient resources """
    insufficient = []

    for item in menu[coffee]["ingredients"]:
        if menu[coffee]["ingredients"][item] > resources[item]:
            insufficient.append(item)

    if insufficient:
        print(f"Sorry, there is not enough {", ".join(insufficient)}.") #it will combine all elements in the list 
           
        
def update_resources(coffee):
    """it will update the resources with each order, minus resources as they used """
    if coffee == "espresso":
       resources["water"] -= menu[coffee]["ingredients"]["water"]
       resources["coffee"] -= menu[coffee]["ingredients"]["coffee"]
    else:
        resources["water"] -= menu[coffee]["ingredients"]["water"]
        resources["coffee"] -= menu[coffee]["ingredients"]["coffee"]
        resources["milk"] -= menu[coffee]["ingredients"]["milk"]



is_coffee_machine_off= False

while not is_coffee_machine_off:
       order = input(f"​What would you like? (espresso/latte/cappuccino) ​") 
        
       if order == "report":
          for item in resources:
              print(f"{item}: {resources[item]}")
       elif order == "off":
           is_coffee_machine_off = True
       else:
            if resource_enough(order):
                coin = coin_input()
                change = coin_process(order, coin)
                if change == "no" :
                    print(f"Not enough money , we refunded your {coin} rupees")
                elif change >=0:
                    name = input("what is your name sir/maam ").title()
                    print(f" Enjoy your {order} {name} ")
                    update_resources(order)
                    if change>0:
                         print(f"and here is your change {change} ") 
                else:
                    None    

            else:
                resources_check(order)    






      



         
      


    


      
              


