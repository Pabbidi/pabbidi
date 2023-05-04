import string

# Define the valid characters for the cipher
valid_chars = string.ascii_lowercase + string.digits + ' '

def create_cipher_keys(key):
    # Create a list of cipher keys based on the given key
    keys = []
    for i in range(len(key)):
        shift = ord(key[i]) - ord('a')
        keys.append(''.join([chr((j+shift)%26 + ord('a')) for j in range(26)]))

    return keys

def encrypt(plaintext, keys):
    # Encrypt the plaintext using the given cipher keys
    ciphertext = ""
    key_index = 0
    for char in plaintext.lower():
        if char in valid_chars:
            shift = ord(keys[key_index][ord(char)-ord('a')]) - ord('a')
            ciphertext += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            key_index = (key_index + 1) % len(keys)
        else:
            ciphertext += char

    return ciphertext

# Example usage:
key = "secretkey"
keys = create_cipher_keys(key)
plaintext = "the quick brown fox jumps over the lazy dog"
ciphertext = encrypt(plaintext, keys)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
