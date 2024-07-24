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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
""" steps for making coffee machine """
#1prompt "what would you like ?(espresso/latte/cappuccino)
#drink_choice=input("what would you like ?(espresso/latte/cappuccino)").upper()
#2show the price : "please insert this amount of money " when they give more , you  give back the change , if less sorry it's not enough ! Money refunded
price={
    "espresso_price": 2.0,
    "latte_price": 4.0,
    "cappucino_price": 4.0
}
while True :
    drink_choice=input("what would you like ?(espresso/latte/cappuccino)")
    #def check_ingredients(): we mean by the resources
    def check_ingredients(menu_item, MENU, resources):
        global drink_choice
        ingredients = MENU[menu_item]["ingredients"]

        for ingredient, amount in ingredients.items():
            if amount > resources.get(ingredient, 0):
                print("Insufficient resources.")
                return

        print("Sufficient resources.")
        for ingredient, amount in ingredients.items():
            resources[ingredient] -= amount
            report= resources[ingredient]

        #check_ingredients(drink_choice, MENU, resources)
        def check_price():
            global drink_choice
            # 1prompt "what would you like ?(espresso/latte/cappuccino)
            # 2show the price :
            if drink_choice == "espresso":
                print(f" the price is : { price['espresso_price']}")
            elif drink_choice == "latte":
                print(f"the price is :{price['latte_price']}")
            elif drink_choice=="cappuccino":
                print(f"the price is :{price['cappucino_price']}")
        check_price()
        refund=0
        cost=0
        # Retrieves the price for the selected drink based on the drink_choice.
        drink_price = price.get(f"{drink_choice}_price", 0)
        coins = 0.0  # Initialize the coins variable
        #checkin if the coins are successfully inserted and match the price before preparing the drink
        while coins < drink_price:
            additional_coins = float(input("Insert your money: $"))  # Use float for currency
            coins += additional_coins

            if coins == drink_price:
                print("Exact amount received. Thank you!😊")
                print(" we are preparing your drink :>")
                print("☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕☕")
                break  # Exit the loop
            elif coins > drink_price:
                refund = coins - drink_price
                print(f"Please take your ${refund:.2f} refund.")
                break  # Exit the loop
            elif coins < drink_price:
                cost = drink_price - coins
                print(f"You still need to insert ${cost:.2f} to proceed.")
                choice= input("do you still want your drink , yes or no?").upper() # Check if they want to proceed or leave
                if choice =="no":
                    print(f" here is your money back : {additional_coins}")
                    break
                else:
                    continue
        #Preparing the drink :
        #print report

        print("Here is the report about the resources left:", resources)

    check_ingredients(drink_choice, MENU, resources)
    another_drink=input(" do you want another drink ? , type yes or no 🤔")
    if another_drink=="no":
        print("thank you , see you around 😄 ")
        break
#4 once the drink is ready  print ("Action has completed")
#5 print("report")
#6 here is your "drink"  enjoy!
#5turn off  the machine ( ask if the user want to turn off the machine if its off then loop stops)


