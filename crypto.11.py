import math
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
num_combinations = math.comb(len(alphabet), 2)
num_permutations = math.perm(num_combinations, 2)
num_keys = num_permutations / 2
print(f"The Playfair cipher has approximately {int(num_keys)} possible keys.")

