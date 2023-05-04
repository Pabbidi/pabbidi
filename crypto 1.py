def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result += shifted_char
        elif char.islower():
            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result += shifted_char
        else:
            result += char

    return result
text = "Hello, World!"
for shift in range(1, 26):
    print(f"Shift {shift}: {caesar_cipher(text, shift)}")
