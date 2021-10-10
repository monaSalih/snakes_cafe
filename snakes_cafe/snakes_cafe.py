print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
menuList = {"wings":0, "cookies":0, "spring rolls":0, "salmon":0, "salmon":0, "steak":0, "meat tornado":0,
            "a literal garden":0, "ice cream":0, "cake":0, "pie":0, "coffee":0, "tea":0, "unicorn tears":0}

# userInput = input('plz inter your order> ').lower()
userOrder = []


# def resturentOrder():
userInput = input('plz inter your order> ').lower()
while userInput != "quit":

    if userInput in menuList:
        menuList[userInput]=menuList[userInput]+1
        for i in menuList:
            if menuList[i]>0:
                print("{} order of {} have been added to your meal".format(
                    menuList[i], i))
    else :
        print("this order not in our menu please try again we work to add it")
        menuList[userInput]=0
        # print("{} order of {} we have been added to your meal".format(
        #             menuList[userInput], userInput))
    userInput = input('plz inter your order \n > ').lower()
        
        
