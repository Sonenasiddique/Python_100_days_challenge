# Trasure iSland coding 




print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=._o._; | ;_.--"o.--"_/______/______/____
''')


print("Welcome  to Treasure Island \nYour mission is to find the treasure .")
pick_1 = input("your are at a crossroad, where do youwant to go? Type 'Left' or 'Right' ").lower()

if pick_1 == 'left':
    print("you can continue your treasure finding path :")
    pick2 = input("you hve come to lake there is an island you want to swim or wait ? Type 'Swim' or  'Wait' ").lower()
    if pick2 == 'wait':
        print("cograts! you have Reach the 2nd level .")
        pick3 = input("Which Door  you Want  to choose ? Type  'Red'  , 'Blue' or  'Yellow' ").lower()
        if pick3 =='yellow' :
            print("Congrats! YOU Reach the treasure. \nYou Win")
        elif pick3 ==  'red' :
            print("Opps!  you are one level  away . \n Game Over")
        else :
            print("Unfortunately you loss. \nGame Over")
    else:
        print("Ohh Sorry you loss . \nGame Over .")
else:
    print("You  Fall into Trap . \nGame  Over ")







