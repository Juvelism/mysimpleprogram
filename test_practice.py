from cypher_text import logo

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

    return  encrypt_message

def decrypt(text,shifts):
    decrypt_message = ""
    for letter in text:
        message = alphabet.index(letter)
        index_message = message - shifts
        range_index = index_message % len(alphabet)
        shifted_message = alphabet[range_index]
        decrypt_message += shifted_message

    return decrypt_message

def main():
    print(logo)
    is_over = False
    while not is_over:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

        if direction != "encode" and direction != "decode":
            print("Invalid input")
            is_over = True
        else:
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            if direction == "encode":
                en = encrypt(text,shift)
                print(f"Here's the {direction} result : {en}")
            elif direction == "decode":
                de = decrypt(text,shift)
                print(f"Here's the {direction} result : {de}")

            again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
            if again == "yes":
                main()
            else:
                is_over = True
                print("Goodbye")
main()