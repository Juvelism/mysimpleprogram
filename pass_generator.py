import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l','m',
           'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generated_list = []

for i in range(1, nr_letters + 1 ):
    generated_list.append(random.choice(letters))

for i in range(1, nr_symbols + 1 ):
    generated_list.append(random.choice(numbers))

for i in range(1, nr_symbols + 1 ):
    generated_list.append(random.choice(symbols))

generated_pw = ''

print(generated_list)
random.shuffle(generated_list)

for f in generated_list:
    generated_pw += f

print(generated_list)
print(f'Your password is: {generated_pw}')

