

message = "Hello world!"
permutation = [8, 5, 7, 6, 4, 2, 3, 10, 9, 1, 0, 11]


def transposition_encrypt(plaintext, perm):
    ciphertext = [""] * len(plaintext)
    if len(perm) != len(plaintext):
        return "Length of permutation list length must match the length of the plaintext."
    for i in range(len(plaintext)):              # For each character in the plaintext
        ciphertext[perm[i]] = plaintext[i]       # send the character to its permuted position.
    return "".join(ciphertext)


def transposition_decrypt(ciphertext, perm):
    plaintext = [""] * len(ciphertext)
    if len(perm) != len(ciphertext):
        return "Length of permutation list length must match the length of the ciphertext."
    for i in range(len(ciphertext)):
        plaintext[perm.index(i)] = ciphertext[i]    # Return the permuted characters to their original positions.
    return "".join(plaintext)


print(transposition_encrypt("Hello World!", permutation))
print(transposition_decrypt("dl WoellHro!", permutation))









