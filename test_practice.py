import random

words = ["abcd", "efgh", "ijkl"]
random_words = random.choice(words)
print(random_words)

letter_display = []

while True:

    guess = input("Guess a letter: ")

    if guess in letter_display:
        print("You already guessed.")
        continue

    letter_display.append(guess)

    if guess not in random_words:
        print("Wrong guess")

    display = ""

    for letters in random_words:
        if letters in letter_display:
            display += letters
        else:
            display += "_"

    if "_" not in display:
        print("You won the game!")
        break

    print(display)
