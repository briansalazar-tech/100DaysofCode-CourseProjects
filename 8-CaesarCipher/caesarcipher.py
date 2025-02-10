from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, original_text, shift_amount):
    
    output_text = ""

    if direction == "decode":
        shift_amount *= -1

    for character in original_text:
        if character not in alphabet:
            print(character)
            output_text += character
        else:
            shifted_index = alphabet.index(character) + shift_amount
            # If shifted amount is greater than the last index of the alphabet, then index wraps around to begining
            if shifted_index > 25:
                shifted_index = shifted_index % len(alphabet)
            output_text += alphabet[shifted_index]
        
    print(f"Your {direction}d result is: {output_text}") 

while True:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # ensure that encode or decode is entered before proceeding
    if direction != "encode" and direction != "decode":
        print(f"{direction} is not a valid input. Type encode or decode.")
        continue
    text = input("Type your message:\n").lower()
    # Ensure that a valid number is entered
    try:
        shift = int(input("Type the shift number:\n"))
    except:
        print(f"Invalid input. Please enter a number.")
        continue
    
    caesar(direction, text, shift)

    prompt_again = input("Type 'yes' of you want to enter another another message. Otherwise type 'no' to exit.\n").lower()
    if prompt_again[0] != "y":
        break