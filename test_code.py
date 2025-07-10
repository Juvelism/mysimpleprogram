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

is_guessing_game = True
storing_display = []

while is_guessing_game:
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess in chosen_word:
        storing_display.append(guess)

  # TODO-2: Change the for loop so that you keep the previous correct letters in display.



    print(storing_display)