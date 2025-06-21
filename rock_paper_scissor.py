import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# CODE stars here

game = [rock, paper, scissors]

while True:
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
    if player >= 3 or player < 0:
        print("Invalid, You Lose!")
        break

    comp = random.randint(0,2)

    print(game[player])
    print("Choice ")
    print(game[comp])

    if (player == 0 and comp == 2) or (player == 2 and comp == 1) or (player == 1 and comp ==  0):
        print("You Win!")
    elif player == comp:
        print("It's Tie")
    else:
        print("You Lose!")
