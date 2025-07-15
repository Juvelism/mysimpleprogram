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

    if len(guess) > 2:
        print("Only 1 letter.")

    else:

        if guess in temporary_display:
            print("You already guessed")
            continue

        temporary_display.append(guess)

        for letter in world_holder:
            if letter in temporary_display:
                display += letter
            else:
                display += "_"

        if display == display_word:
            is_game_over = True


        # print(temporary_display)
        print(display)
print("You win")