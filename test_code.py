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
    words = word_generator()

    for char in words:
        if guess_letter == char:
            display += guess_letter
        else:
            display += '_'

    print(display)

def display_output(generated_word):
    print(generated_word)

def main():
    random_word = word_generator()
    display_output(random_word)
    char_display(random_word)
    user_choice()



main()