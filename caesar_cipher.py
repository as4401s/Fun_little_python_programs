alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function for encryption
def encrypt(text, shift):
    print('Original message:', text)
    print('Shift amount:', shift)
    new_string = ''

    for char in text:
        if char in alphabet:  # Only encrypt alphabetic characters
            position = alphabet.index(char)  # Find the index of the character in the alphabet
            position_new = (position + shift) % 26  # Use modulus to wrap around the alphabet
            new_char = alphabet[position_new]  # Get the new character after shifting
            new_string += new_char
        else:
            new_string += char  # Non-alphabet characters are not changed

    return new_string

# Function for decryption
def decrypt(text, shift):
    print('Original message:', text)
    print('Shift amount:', shift)
    new_string = ''

    for char in text:
        if char in alphabet:  # Only decrypt alphabetic characters
            position = alphabet.index(char)  # Find the index of the character in the alphabet
            position_new = (position - shift) % 26  # Subtract shift and use modulus to wrap around the alphabet
            new_char = alphabet[position_new]  # Get the new character after shifting back
            new_string += new_char
        else:
            new_string += char  # Non-alphabet characters are not changed

    return new_string

# User input for choosing encrypt or decrypt and processing text
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encoded_text = encrypt(text, shift)
    print('Encoded message:', encoded_text)
elif direction == 'decode':
    decoded_text = decrypt(text, shift)
    print('Decoded message:', decoded_text)
else:
    print("Invalid choice, please type 'encode' or 'decode'.")

