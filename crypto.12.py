key = np.array([[9, 4], [5, 7]])
plaintext = "meetmeattheusualplaceattenratherthaneightoclock".upper()
plaintext = plaintext.replace("J", "I")
plaintext = [ord(c) - 65 for c in plaintext] 
if len(plaintext) % 2 == 1:
    plaintext.append(23) 
pairs = [np.array([plaintext[i], plaintext[i+1]]).reshape(2, 1) for i in range(0, len(plaintext), 2)]
ciphertext = ""
for pair in pairs:
    product = np.matmul(key, pair) % 26
    ciphertext += chr(product[0][0] + 65) + chr(product[1][0] + 65)

print(ciphertext)
