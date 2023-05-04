def mod_inverse(a, m):
    for i in range(m):
        if (a*i) % m == 1:
            return i
    return -1

def break_affine_cipher(most_freq, second_freq):
    # calculate frequency differences
    freq_diff = ord(most_freq) - ord(second_freq)
    if freq_diff < 0:
        freq_diff += 26
    for a in range(1, 26):
        if a % 2 == 0 or a % 13 == 0:
            continue
        else:
            inverse = mod_inverse(a, 26)
            b = (ord(most_freq) - (a * (ord('E') - ord('A'))) * inverse) % 26
            if b < 0:
                b += 26
            print(f"a: {a}, b: {b}")
