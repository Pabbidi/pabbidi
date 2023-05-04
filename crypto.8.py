import string

def generate_cipher(keyword):
    unique_chars = []
    for char in keyword.upper():
        if char not in unique_chars and char in string.ascii_uppercase:
            unique_chars.append(char)
    for char in string.ascii_uppercase:
        if char not in unique_chars:
            unique_chars.append(char)
    cipher_dict = {}
    for i in range(len(string.ascii_uppercase)):
        cipher_dict[string.ascii_uppercase[i]] = unique_chars[i]
    
    return cipher_dict
cipher_dict = generate_cipher("CIPHER")
plaintext = "HELLO WORLD"
ciphertext = ""
for char in plaintext:
    if char.upper() in cipher_dict:
        ciphertext += cipher_dict[char.upper()]
    else:
        ciphertext += char
print(ciphertext)
