key = 'MFHIJKNOPQUZVWXYELARGDSTBC'
matrix = [key[i:i+5] for i in range(0, 25, 5)]
def get_indices(c):
    for i, row in enumerate(matrix):
        for j, letter in enumerate(row):
            if letter == c:
                return (i, j)
def encrypt(message):
    # Replace J with I
    message = message.upper().replace('J', 'I')

    message = ''.join(filter(str.isalpha, message))
    if len(message) % 2 != 0:
        message += 'Z'
    pairs = [message[i:i+2] for i in range(0, len(message), 2)]
    ciphertext = ''
    for pair in pairs:
        row1, col1 = get_indices(pair[0])
        row2, col2 = get_indices(pair[1])

        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5]
            ciphertext += matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext += matrix[(row1+1)%5][col1]
            ciphertext += matrix[(row2+1)%5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext
