MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit =0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(orderingrdient):
    for item in orderingrdient :
        if orderingrdient[item] > resources[item]:
            print(f"there is not enough {item}")
            return False
    return True
def process_coins():
    """retrun the total calculated from coins inserted """
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total
def is_trnsiction_sucsessful(money_recieved,drink_cost):
    """Return True when the payement is accepted or false when it is insuffecient."""
    if money_recieved >= drink_cost:
        change =round(money_recieved - drink_cost,2)
        print(f"Here is in {change} change")
        global profit
        profit += drink_cost
        return True
    else :
        print("Sorry ther's not enough Money , Money refouded.")
        return False
def make_coffe(drink_name,order_ingredient):
    """deduct the required ingrdients from resoursces """
    for item in order_ingredient:
        global resources
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}☕")

is_on = True
while is_on:
    choice=input(" What would you like ? (espresso,latte,cappuccino =>:")
    if choice =="off":
        is_on =False
    elif choice =="report":

        print(f"water:{resources['water']} ml")
        print(f"milk:{resources['milk']} ml")
        print(f"coffee:{resources['coffee']} g")
        print(f"Money:{profit}$")
    else:
        drink = MENU[choice]
        # print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment =process_coins()
            if is_trnsiction_sucsessful(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])
    

