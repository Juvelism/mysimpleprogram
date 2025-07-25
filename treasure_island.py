print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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


print("You're at a cross road. Where do you want to go?")
first_stage = input('Type "left" or "right"\n').lower()
if first_stage == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    second_stage = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if second_stage == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        third_stage = input("One red, one yellow and one blue. Which color do you choose?\n").lower()
        if third_stage == "yellow":
            print("You found the treasure! You Win!")
        elif third_stage == "red":
            print("Burned by fire. Game Over.")
        elif third_stage == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")

    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
