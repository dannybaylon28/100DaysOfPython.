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
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
path = input("Choose your path. Left or Right? \n").lower()

if path == "left":
    river = input("You chose left. You're in front of a river. You swim trought it or you just wait?\n").lower()

    if river == "wait":
        print("A boat came and picked you up. The boat leaves you in front of a castle with 3 different doors.")
        door = input("Which door do you pick? \n Red, Yellow or Blue?\n").lower()

        if door == "yellow":
            print("CONGRATULATIONS YOU WIN!!!")
        elif door == "blue":
            print("You got eaten by beasts. \n GAME OVER!!!")
        elif door == "red":
            print("You got burned by fire. \n GAME OVER!!!")
        else:
            print("That's not even an option. \n GAME OVER!!!")

    else:
        print("You get attacked by a trout.\n GAME OVER!!!")

else:
    print("You fell into a hole. \n GAME OVER!!!")
    

