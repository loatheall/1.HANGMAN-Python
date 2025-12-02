from art import start

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

again = False


# TODO-1: Combine the encrypt() and decrypt() into a single function 'caesar()'
#  Use the value of the user chosen 'direction' variable to determine which functionality to use
#  Call the caesar function instead of encrypt/decrypt and pass all 3 variables direction/text/shift
def caesar(encode_or_decode, original_text, shift_amount):
    cipher_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char in alphabet:
            number = alphabet.index(char)
            index_after_shift = (number + shift_amount) % len(alphabet)
            cipher_text += alphabet[index_after_shift]
        else:
            cipher_text += char

    print(f"Here is the {encode_or_decode}d result: {cipher_text}")



while not again:
    print(start)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    if direction != "encode" and direction != "decode":
        print("Invalid direction")

    else:
        text = input("Type your message:\n ").lower()
        shift = int(input("Type the shift number:\n "))

        caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)


    choice = input("Do you want to continue? (y/n): ").lower()

    if choice == "n":
        again = True
        print(f"{start}\nThank you for playing!")
