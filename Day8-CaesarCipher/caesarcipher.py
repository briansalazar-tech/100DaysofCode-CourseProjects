alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        shifted_index = alphabet.index(letter) + shift_amount
        # If shifted amount is greater than the last index of the alphabet, then index wraps around to begining
        if shifted_index > 25:
            shifted_index = shifted_index % 26
        encrypted_text += alphabet[shifted_index]
    print(encrypted_text)


encrypt(text, shift)