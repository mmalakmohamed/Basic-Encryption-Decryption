text = input("Enter the text you want to encrypt: ")
shift = int(input("Enter the shift key: "))
encrypted_text = ""

for char in text:
    if char.isalpha():
        if char.isupper():
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        encrypted_text += char
        print("Original text:", text)
print("Encrypted text:", encrypted_text)
decrypted_text = ""

for char in encrypted_text:
    if char.isalpha():
        if char.isupper():
            decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
    else:
        decrypted_text += char

print("Decrypted text:", decrypted_text)