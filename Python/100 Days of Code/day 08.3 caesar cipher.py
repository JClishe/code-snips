

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    
    for i in plain_text:
        """
        old_position = alphabet.index(i)
        new_position = old_position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
        """
        cipher_text += alphabet[(alphabet.index(i) + shift_amount)]
    
    print(" ")
    print(f"The encoded text is {cipher_text}")


encrypt(plain_text = text, shift_amount = shift)

