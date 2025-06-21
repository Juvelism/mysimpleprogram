import random
import rock_paper_scissor_source

# CODE stars here

game = [rock_paper_scissor_source.rock, rock_paper_scissor_source.paper, rock_paper_scissor_source.scissors]

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
