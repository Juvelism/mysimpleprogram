import random
random_words = ["abdomen", "baywatch", "iglob"]

# Generate random word
world_holder = ""
display_word = random.choice(random_words)
world_holder += display_word
print(world_holder)

underscore_display = ""
for letters in range(len(display_word)):
    underscore_display += "_"
print(underscore_display)

is_game_over = False
temporary_display = []

while not is_game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    if guess in temporary_display:
        print("You already guessed")
        continue

    temporary_display.append(guess)

    for letter in display:
        if letter == guess:
            display += guess
        else:
            display += "_"


    print(temporary_display)
    print(display)