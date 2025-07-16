from hangman_stages import stages
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
lives = 6

while not is_game_over:
        guess = input("Guess a letter: ").lower()

        display = ""

        if guess in temporary_display:
            print("You already guessed")
            continue

        temporary_display.append(guess)

        for letter in world_holder:
            if letter in temporary_display:
                display += letter
            else:
                display += "_"


        print(display)

        if "_" not in display:
            is_game_over = True
            print("You win")

        if guess not in display:
            print(stages[lives])
            lives -= 1

        if lives == 0:
            is_game_over = True
            print("You lose.")

