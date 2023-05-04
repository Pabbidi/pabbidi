import string
valid_chars = string.ascii_lowercase.replace('j', '') + string.digits + ' '

def create_matrix(key):
    key = ''.join(filter(lambda char: char in valid_chars, key.lower()))
    chars = set(valid_chars)
    chars -= set(key)
    chars = list(key) + list(chars)
    matrix = [chars[i:i+5] for i in range(0, len(chars), 5)]

    return matrix

def find_letter(letter, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == letter:
                return (i, j)
    return None

def encrypt(plaintext, matrix):
    pairs = []
    plaintext = plaintext.lower().replace('j', 'i')
    i = 0
    while i < len(plaintext):
        if i+1 < len(plaintext) and plaintext[i] == plaintext[i+1]:
            pairs.append((plaintext[i], 'x'))
            i += 1
        elif i == len(plaintext)-1:
            pairs.append((plaintext[i], 'x'))
        else:
            pairs.append((plaintext[i], plaintext[i+1]))
            i += 2
    ciphertext = ""
    for pair in pairs:
        pos1 = find_letter(pair[0], matrix)
        pos2 = find_letter(pair[1], matrix)
        if pos1[0] == pos2[0]:
            ciphertext += matrix[pos1[0]][(pos1[1]+1)%5]
            ciphertext += matrix[pos2[0]][(pos2[1]+1)%5]
        elif pos1[1] == pos2[1]:
            ciphertext += matrix[(pos1[0]+1)%5][pos1[1]]
            ciphertext += matrix[(pos2[0]+1)%5][pos2[1]]
        else:
            ciphertext += matrix[pos1[0]][pos2[1]]
            ciphertext += matrix[pos2[0]][pos1[1]]

    return ciphertext
