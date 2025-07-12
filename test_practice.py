import random

words = ["abcd", "efgh", "ijkl"]
random_words = random.choice(words)
print(random_words)

holder = ""
for h in range(len(random_words)):
    holder += "_"
print(holder)

letter_display = []
lives = 5

while lives > 0:

    guess = input("Guess a letter: ")

    if guess in letter_display:
        print("You already guessed.")
        continue

    letter_display.append(guess)

    if guess not in random_words:
        lives -= 1

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
    print(lives)

else:
    print("You lose!")