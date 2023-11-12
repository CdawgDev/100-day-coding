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

two_road = input("You come across a two roads would you like to go left or right?\n").lower()

if two_road == "right":
    swim = input("After traveling down the road you are met with a large river. Do you want to swim or wait?\n").lower()
    if swim == "swim":
        print("You starting swimming. Then suddenly a gaint shark comes from behind you and eats you. Game Over.")
    else:
        doors = input("You choose to wait. The water in the river slowly dries up and revels 3 colored doors. red blue or yellow?\n").lower()
        if doors == "yellow":
            print("You open the door and there lies a chest full of golden coins. You Win!")
        if doors == "blue":
            print("You open a door to a nest of killer ants. They swarm you and you die. Game Over.")
        if doors == "red":
            print("You open a door to a dragons nest. The dragon blows fire at you before you have time to move. Game Over.")

else:
    print("You try going left and trip and impale yourself on a stick. Game Over.")