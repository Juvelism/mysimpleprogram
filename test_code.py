from hangman_stages import stages

for item in reversed(range(len(stages))):
    user_input = input("Guess a letter: ")
    if user_input == "1":
        print("Correct!")
    else:
        print(stages[item])
