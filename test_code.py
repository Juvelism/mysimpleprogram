import random
from itertools import count

from sample_score_calculation import get_student

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l','m',
           'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def get_number():
    get_turn = int(input("How many? "))
    return get_turn

def pick_random(source,pick):
    generated_list = []

    for i in range(0, pick):
        generated_list.append(random.choice(source))

    return generated_list

def main():
    turn = get_number()
    pick_random(letters,turn)

main()