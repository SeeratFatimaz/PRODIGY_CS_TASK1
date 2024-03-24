def caesar_cipher(text, shift, decrypt=False):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shift_factor = -shift if decrypt else shift
            encrypted_text += chr((ord(char) - offset + shift_factor) % 26 + offset)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    while True:
        choice = input("Choose 'E' for encryption or 'D' for decryption: ").upper()
        if choice in ['E', 'D']:
            break
        else:
            print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")

    message = input("Enter the message: ")

    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift value.")

    if choice == 'E':
        print("Encrypted message:", caesar_cipher(message, shift))
    elif choice == 'D':
        print("Decrypted message:", caesar_cipher(message, shift, decrypt=True))

if __name__ == "__main__":
    main()