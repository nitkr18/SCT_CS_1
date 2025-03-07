def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            pos = ord(char) - ord('A')
            new_pos = (pos + shift) % 26
            new_char = chr(new_pos + ord('A'))
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_message(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            pos = ord(char) - ord('A')
            new_pos = (pos - shift) % 26
            new_char = chr(new_pos + ord('A'))
            decrypted_message += new_char
        else:
            decrypted_message += char
    return decrypted_message

message = "THE HOUSE IS NOW FOR SALE"
shift_value = 5

encrypted = encrypt_message(message, shift_value)
print("Encrypted Message:", encrypted)

decrypted = decrypt_message(encrypted, shift_value)
print("Decrypted Message:", decrypted)
