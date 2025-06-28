import random

def user_choice():
    user = input('Guess a letter: ')
    return user

def word_generator():
    word_list = ["aardvark", "baboon", "camel"]
    guess_word = random.choice(word_list)
    return guess_word

def char_display(guess_letter):

    display = ''

    for char in guess_letter:
        if guess_letter == char:
            display += guess_letter
        else:
            display += '_'

    return display

def display_view(pick_word,guess_w):
    print(pick_word)
    print(guess_w)

def main():
    letter_convert = word_generator()
    display_view(letter_convert,char_display(letter_convert))
    user_choice()


main()