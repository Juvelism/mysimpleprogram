import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.

first_display = []

is_game = True

while is_game:
    guess = input("Guess a letter: ").lower()

    display = ""

    if guess in first_display:
        print("You've already guessed that letter.")

    if guess == chosen_word:
        first_display.append(guess)
    else:
        first_display.append("_")


# TODO-2: Change the for loop so that you keep the previous correct letters in display.

    print(first_display)