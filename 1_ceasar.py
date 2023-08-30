def caesar_encrypt(message, key):
    encrypted_message = ""
    
    for ch in message:
        if 'a' <= ch <= 'z':
            encrypted_ch = chr(((ord(ch) - ord('a') + key) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            encrypted_ch = chr(((ord(ch) - ord('A') + key) % 26) + ord('A'))
        else:
            encrypted_ch = ch  # Keep non-alphabet characters unchanged
        encrypted_message += encrypted_ch
    
    return encrypted_message

def caesar_decrypt(encrypted_message, key):
    decrypted_message = ""
    
    for ch in encrypted_message:
        if 'a' <= ch <= 'z':
            decrypted_ch = chr(((ord(ch) - ord('a') - key) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            decrypted_ch = chr(((ord(ch) - ord('A') - key) % 26) + ord('A'))
        else:
            decrypted_ch = ch  # Keep non-alphabet characters unchanged
        decrypted_message += decrypted_ch
    
    return decrypted_message

message = input("Enter the message: ")
key = int(input("Enter key: "))
choice = int(input("Enter your choice\n1. Encryption\n2. Decryption\n"))

if choice == 1:
    encrypted_message = caesar_encrypt(message, key)
    print("Encrypted message:", encrypted_message)
elif choice == 2:
    decrypted_message = caesar_decrypt(message, key)
    print("Decrypted message:", decrypted_message)
