import random
import rock_paper_scissor_source

# CODE stars here

game = [rock_paper_scissor_source.rock, rock_paper_scissor_source.paper, rock_paper_scissor_source.scissors]
p_score = 0
c_score = 0

# This while loop continue if player or computer reach the number of games (5).
while p_score or c_score != 5:
    player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

    # Check if player input is valid.
    if player >= 3 or player < 0:
        print("Invalid input, Game over!")
        break

    # If valid proceed to computer random number.
    comp = random.randint(0,2)

    print(game[player])
    print("Computer choice: ")
    print(game[comp])

    # Checking who win to gain score
    if (player == 0 and comp == 2) or (player == 2 and comp == 1) or (player == 1 and comp ==  0):
        p_score += 1
        print("You Win!")
    elif player == comp:
        print("It's Tie")
    else:
        c_score += 1
        print("You Lose!")

    # Printing the current score
    print(f"Player score: {p_score} | Computer score: {c_score}")

    # Checking if player or computer reach the number of rounds. To win the game.
    if p_score == 5:
        print("Player Won the game!")
        break
    elif c_score == 5:
        print("Computer Won the game!")
        break