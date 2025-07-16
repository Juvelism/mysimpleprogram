# HANGMAN

import random
from hangman_words import word_list

words_display =  ""
random_words = random.choice(word_list)
words_display += random_words
print(words_display)

words_convert = ""
for num in range(len(random_words)):
    words_convert += "_"
print(words_convert)

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ")

    display = ""

    for letter in random_words:
        if letter in correct_letter:
            display += letter
            correct_letter.append(guess)
        elif letter == guess:
            display += letter
        else:
            display += "_"

    print(display)