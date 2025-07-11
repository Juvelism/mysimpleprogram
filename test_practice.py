import random

random_words = ["table", "chair", "longboard"]

holder = ""
get_words = random.choice(random_words)
print(get_words)
for letters in range(len(get_words)):
    holder += "_"
print(holder)

################################################

