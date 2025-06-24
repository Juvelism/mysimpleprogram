import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l','m',
           'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Simple Password Generator by Juvs!")

def get_number():
    get_letter = int(input("How many letters? "))
    get_num = int(input("How many numbers? "))
    get_symbol = int(input("How many symbols? "))

    return get_letter, get_num, get_symbol

def pick_random(source,pick):
    generated_list = []

    for i in range(0, pick):
        generated_list.append(random.choice(source))

    return generated_list

def show_result(generate_pass):
    print(generate_pass)
    random.shuffle(generate_pass)
    print(generate_pass)

    g_list = ''

    for i in generate_pass:
        g_list += i

    print(f'You password is: {g_list}')

def main():
    turn_1, turn_2, turn_3 = get_number()
    final_list = (pick_random(letters,turn_1)) + (pick_random(numbers, turn_2)) + (pick_random(symbols, turn_3))
    show_result(final_list)

main()