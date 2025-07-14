import random
words = ["abdomen", "baywatch", "iglob"]

# Generate random word
world_holder = ""
display_word = random.choice(words)
world_holder += display_word
print(world_holder)

underscore_display = ""
for letters in range(len(display_word)):
    underscore_display += "_"
print(underscore_display)


is_game_over = True

while is_game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in display_word:
        if letter == guess:
            display += letter
        else:
            display += "_"

    print(display)