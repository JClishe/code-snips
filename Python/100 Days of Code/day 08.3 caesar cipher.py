

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

reverse_alphabet = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', 'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

def caesar(method, message, shift_amount):
    cipher_text = ""

    if method == "encode":
        for i in message:
            if i in alphabet:
                cipher_text += alphabet[(alphabet.index(i) + shift_amount)]
            else:
                cipher_text += i
        
    elif method == "decode":
        for i in message:
            if i in reverse_alphabet:
                cipher_text += reverse_alphabet[(reverse_alphabet.index(i) + shift_amount)]
            else:
                cipher_text += i

    print(f"The {direction}d text is {cipher_text}\n")

execute = True

while execute:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift >= 26:
        shift = int(input("Please enter a shift amount between 0 - 25:\n"))

    caesar(method=direction, message=text, shift_amount=shift)

    result = input("Would you like to play again yes/no? ").lower()

    if result == "no":
        execute = False
        print("Goodbye")

