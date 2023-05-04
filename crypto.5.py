import string
valid_chars = string.ascii_lowercase + string.digits + ' '

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, y, x = egcd(b, a % b)
        return g, x, y - (a // b) * x

def mod_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % m

def create_cipher_keys(a, b):
    keys = [(a*i+b)%26 for i in range(26)]

    return keys

def encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext.lower():
        if char in valid_chars:
            plaintext_index = ord(char) - ord('a')
            ciphertext_index = create_cipher_keys(a, b)[plaintext_index]
            ciphertext += chr(ciphertext_index + ord('a'))
        else:
            ciphertext += char

    return ciphertext
a = 3
b = 7
plaintext = "the quick brown fox jumps over the lazy dog"
ciphertext = encrypt(plaintext, a, b)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
