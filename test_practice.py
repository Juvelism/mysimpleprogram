alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    encrypt_message = ""
    for letter in original_text:
        message = alphabet.index(letter)
        index_message = message + shift_amount
        range_index = index_message % len(alphabet)
        shifted_message = alphabet[range_index]
        encrypt_message += shifted_message

    print(f"Encrypted message: {encrypt_message}")
def decrypt(text,shifts):
    decrypt_message = ""
    for letter in text:
        message = alphabet.index(letter)
        index_message = message - shifts
        range_index = index_message % len(alphabet)
        shifted_message = alphabet[range_index]
        decrypt_message += shifted_message
    print(f"Decrypted message: {decrypt_message}")

def main():
    print("Welcome to Encrypt your Message")
    is_over = False

    while not is_over:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "q":
            is_over = True
        else:
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            if direction == "encode":
                encrypt(text,shift)
            elif direction == "decode":
                decrypt(text,shift)

main()