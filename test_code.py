import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

is_guessing = True

guessed_word = []

lives = 5

while is_guessing:

    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        guessed_word.append(guess)
    else:
        lives -= 1

    display = ""
    for letter in chosen_word:
        if letter in guessed_word:
            display += letter
        else:
            display += "_"


    print(display)
    print(lives)
