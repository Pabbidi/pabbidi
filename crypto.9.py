from playfair import PlayfairCipher
key = 'PTBOATS'
pf = PlayfairCipher(key)
ciphertext = 'KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ'
ciphertext = ciphertext.replace(' ', '')
plaintext = pf.decrypt(ciphertext)
print(plaintext)
