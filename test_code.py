import random

word_list = ["aardvark", "baboon", "camel"]

# Print chosen word
chosen_word = random.choice(word_list)
print(chosen_word)

# Print underscore
placeholder = "_" * len(chosen_word)
print(placeholder)

guess = input("Guess a word: ")
display = ""

for letters in chosen_word:
    if guess == letters:
        display += guess
    else:
        display += "_"

print(display)

