# Password Generator
import random

small_alphabet = ["a","b","c","d","e",
                  "f", "g", "h", "i",
                  "j", "k", "l", "m",
                  "n", "o", "p", "q",
                  "r", "s", "t", "u",
                  "v", "w", "x", "y", "z"]

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

stock_pw = []

a_pw = int(input("How many alphabet characters: "))
n_pw = int(input("How many numbers: "))

stock_pw += random.choices(small_alphabet, k=a_pw) + random.choices(nums, k=n_pw)
random.shuffle(stock_pw)
final_tip = ''.join(stock_pw)
print(f"Generated password: {final_tip}")
