def vigenere_encrypt(message, key):
    encrypted_message = ""
    
    key_length = len(key)
    for i in range(len(message)):
        ch = message[i]
        if 'a' <= ch <= 'z':
            shift = ord(key[i % key_length].lower()) - ord('a')
            encrypted_ch = chr(((ord(ch) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            shift = ord(key[i % key_length].upper()) - ord('A')
            encrypted_ch = chr(((ord(ch) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_ch = ch  # Keep non-alphabet characters unchanged
        encrypted_message += encrypted_ch
    
    return encrypted_message

def vigenere_decrypt(encrypted_message, key):
    decrypted_message = ""
    
    key_length = len(key)
    for i in range(len(encrypted_message)):
        ch = encrypted_message[i]
        if 'a' <= ch <= 'z':
            shift = ord(key[i % key_length].lower()) - ord('a')
            decrypted_ch = chr(((ord(ch) - ord('a') - shift) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            shift = ord(key[i % key_length].upper()) - ord('A')
            decrypted_ch = chr(((ord(ch) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_ch = ch  # Keep non-alphabet characters unchanged
        decrypted_message += decrypted_ch
    
    return decrypted_message

message = input("Enter the message: ")
key = input("Enter key: ")
choice = int(input("Enter your choice\n1. Encryption\n2. Decryption\n"))

if choice == 1:
    encrypted_message = vigenere_encrypt(message, key)
    print("Encrypted message:", encrypted_message)
elif choice == 2:
    decrypted_message = vigenere_decrypt(message, key)
    print("Decrypted message:", decrypted_message)
