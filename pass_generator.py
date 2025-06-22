# Password Generator
import random

small_alphabet = ["a","b","c","d","e",
                  "f", "g", "h", "i",
                  "j", "k", "l", "m",
                  "n", "o", "p", "q",
                  "r", "s", "t", "u",
                  "v", "w", "x", "y", "z"]

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

stocked_pw = []

new_lst = []

a_pw = int(input("How many alphabet characters: "))
if a_pw < 0:
    print("Invalid input!")

n_pw = int(input("How many numbers: "))

stocked_pw += random.choices(small_alphabet, k=a_pw) + random.choices(nums, k=n_pw)

for h in stocked_pw:
    new_lst.append(h)

generated_pw = ""
for f in new_lst:
    generated_pw += f

print(f"Generated Password: {generated_pw}")


