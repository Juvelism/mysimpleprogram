# Pass Generator

import random

small_alphabet = ["a","b","c","d","e",
                  "f", "g", "h", "i",
                  "j", "k", "l", "m",
                  "n", "o", "p", "q",
                  "r", "s", "t", "u",
                  "v", "w", "x", "y", "z"]

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

stock_pw = []

alpha_char = int(input("Enter number of characters: "))
char_list = random.choices(small_alphabet, k=alpha_char)
stock_pw.append(char_list)

alpha_nums = int(input("Enter numbers: "))
num_list = random.choices(nums, k=alpha_nums)
stock_pw.append(num_list)

generated_pw = ''

for letter in stock_pw:
    generated_pw = ''.join(letter)

print(f"Generated Password: {generated_pw}")

