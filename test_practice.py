import random

words = ["abcd", "efgh", "ijkl"]
random_words = random.choice(words)
print(random_words)

letter_display = []

while True:
    guess = input("Guess a letter: ")

    if guess in letter_display:
        print("You already guessed.")
    else:
        letter_display.append(guess)

    display = ""

    for letters in random_words:
        if letters in letter_display:
            display += letters
        else:
            display += "_"

    print(display)