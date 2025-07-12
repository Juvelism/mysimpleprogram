import random

word_list = ["aardvark", "baboon", "camel"]
random_words = random.choice(word_list)
print(random_words)

place_holder = ""
for letters in range(len(random_words)):
    place_holder += "_"
print(place_holder)

placeholder_display = []

while True:
    guess = input("Guess a letter: ")

    if guess in placeholder_display:
        print("You already guessed.")
    else:
        placeholder_display.append(guess)

    display = ""

    for letter in random_words:
        if letter == guess:
            display += guess
        else:
            display += "_"
    print(display)
