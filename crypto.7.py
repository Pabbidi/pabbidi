ciphertext = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83 \
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8* \
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"

cipher_map = {
    '0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h',
    '8': 'i', '9': 'j', ';': 'k', '<': 'l', '=': 'm', '>': 'n', '?': 'o', '@': 'p',
    'A': 'q', 'B': 'r', 'C': 's', 'D': 't', 'E': 'u', 'F': 'v', 'G': 'w', 'H': 'x',
    'I': 'y', 'J': 'z', '(': ' ', ')': ' '
}

plaintext = ''
for c in ciphertext:
    if c in cipher_map:
        plaintext += cipher_map[c]
    else:
        plaintext += c

print(plaintext)
