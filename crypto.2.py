import random
plaintext_alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphertext_alphabet = "qwertyuiopasdfghjklzxcvbnm"

def create_cipher_key():
    cipher_key = {}
    shuffled_alphabet = list(ciphertext_alphabet)
    random.shuffle(shuffled_alphabet)
    for i in range(len(plaintext_alphabet)):
        cipher_key[plaintext_alphabet[i]] = shuffled_alphabet[i]

    return cipher_key

def encrypt(plaintext, cipher_key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ciphertext += cipher_key[char.lower()].upper() if char.isupper() else cipher_key[char]
        else:
            ciphertext += char

    return ciphertext
plaintext = "the quick brown fox jumps over the lazy dog"
cipher_key = create_cipher_key()
ciphertext = encrypt(plaintext, cipher_key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Cipher key:", cipher_key)
