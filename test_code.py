import random

# 1: GENERATE RANDOM WORDS
word_list = ["aardvark", "baboon", "camel"]
random_words = random.choice(word_list)
print(random_words)

# 2: GENERATE AS MANY BLANKS AS LETTERS IN WORD
place_holder = ""
for letters in range(len(random_words)):
    place_holder += "_"
print(place_holder)

# 3
placeholder_display = []
lives = 5

while lives > 0:
    guess = input("Guess a letter: ")

    if guess in placeholder_display:
        print("You already guessed.")
        continue

    placeholder_display.append(guess)

    display = ""

    if guess not in random_words:
        lives -= 1

    for letter in random_words:
        if letter in placeholder_display:
            display += letter
        else:
            display += "_"

    if "_" not in display:
        print(random_words)
        print("You won!")
        break

    print(display)
    print(f'Your lives: {lives}')
else:
    print("You lose!")