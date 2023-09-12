import time
import pandas as pd

#Create a date scenario, introduce the dates name and restaurant.
#plus user inputs the budget for todays date
#included time sleep into the script to make it flow like an actual conversation in the terminal
someName = input("I'm on a date with: ")
print(someName + " where would you like to eat?")
time.sleep(2)
someRes = ("Lets go to olive garden")
print(someRes)
time.sleep(2)
budget = input("whats the budget for today? $")

#Create a menu to choose from (includes items and prices)
#used a pandas import to create a table for the menu and prices

someMenu = ["chicken alfredo", "chicken parm", "eggplant parm","Pizza","water","coca-cola"]
somePrice = [20,22,25,13,2,4]

join = pd.DataFrame({"Item":someMenu , "Price":somePrice})


print("Welcome to oliver garden, Table for two?")
time.sleep(2)
print("certainly follow me this way to your table")
time.sleep(2)
print("heres the menu for today")
time.sleep(3)
print(join)

#Created an empty list for my while loop later on
#myorderfood is to store the items ordered
#myorderprice is to store the prices of the items
#counter is to keep track of the items being ordered
#total is created to add up the whole total after items are ordered
myorderFood=[]
myorderprice=[]
counter=0
Total=0


time.sleep(4)    
order = input("Are you guys ready to order? Yes/No ")
if order == "No":
    print("Ok I'll come back to you")
    exit()
if order =="yes":
    print("Ok what would you like")      
else:
    print("Ok")
    exit()

    nextorder = True

#Created a while loop for when user is placing orders in
#added append to my empty list variable in order for the command to add the menu item to the empty list
#added a counter to have it keep track of the items being ordered
while nextorder == True:
    foodorder = input("What would you like?\n")
    if foodorder == "chicken alfredo":
        myorderFood.append(someMenu[0])
        myorderprice.append(somePrice[0]) 
        counter=counter+1
        Total=Total+(somePrice[0])
    elif foodorder == "chicken parm":  
        myorderFood.append(someMenu[1])
        myorderprice.append(somePrice[1])
        counter=counter+1
        Total=Total+(somePrice[1])
    elif foodorder == "eggplant parm":
        myorderFood.append(someMenu[2])
        myorderprice.append(somePrice[2])
        counter=counter+1
        Total=Total+(somePrice[2])
    elif foodorder == "pizza":
        myorderFood.append(someMenu[3])
        myorderprice.append(somePrice[3])
        counter=counter+1 
        Total=Total+(somePrice[3])
    elif foodorder =="water":
        myorderFood.append(someMenu[4])
        myorderprice.append(somePrice[4])
        counter=counter+1 
        Total=Total+(somePrice[4])
    elif foodorder == "coca-cola":
        myorderFood.append(someMenu[5])
        myorderprice.append(somePrice[5])
        counter=counter+1 
        Total=Total+(somePrice[5])
    finished = input("will that be all? yes/no")
    if finished == "no":
        nextorder = True
    else:
        nextorder = False       

y=0

print ("Heres your receipt\n")
#print ("     ")
print ("********")
while y<counter:

    print ("Item:" + (myorderFood[y]))
    print ("Cost:" + str(myorderprice[y]))
    y=y+1
print ("The final cost will be $"+ str(Total))  
time.sleep(3) 
if Total > 50:
    print("We should go out again sometime")
else:
    print("Alright I'm going home, see you around")
