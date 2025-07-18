alphabet = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j','k','l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

words = input("Enter the word: ")
shift_count = int(input("Enter number: "))

index = len(words)
index_count = alphabet[shift_count]

print(f"word: {words}")
print(f"len of word: {index}")
print(f"shift count: {index_count}")
print(f"{alphabet[index]}")

print(alphabet[index:shift_count+index])