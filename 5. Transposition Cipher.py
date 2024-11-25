
message = "Hello world!"
permutation = [8,5,7,6,4,2,3,10,9,1,0,11]

# For a given message the transposition cipher permutes
# the characters according to the given permutation.

def transposition_encrypt(p, perm):
    c = [""] * len(p)
    if len(perm) != len(p):
        return "Length of permutation list length must match the length of the plaintext."
    for i in range(len(p)):     # For each character in the plaintext
        c[perm[i]] = p[i]       # send the character to its permuted position.
    return "".join(c)           # Join the array of those permuted characters together to form the ciphertext.

def transposition_decrypt(c,perm):
    p = [""] * len(c)
    if len(perm) != len(c):
        return "Length of permutation list length must match the length of the ciphertext."
    for i in range(len(c)):
        p[perm.index(i)] = c[i]     # Analogously, return the permuted characters to their original positions.
    return "".join(p)

print(transposition_encrypt("Hello world!", permutation))
print(transposition_decrypt("dl woellHro!", permutation))









