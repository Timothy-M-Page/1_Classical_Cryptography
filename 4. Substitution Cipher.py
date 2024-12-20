

A = "abcdefghijklmnopqrstuvwxyz"
B = "poiuytrewqasdfghjklmnbvcxz"    # A substitution alphabet


def sub_encrypt(plaintext, sub_alpha):
    ciphertext = ""
    plaintext = plaintext.lower()
    for letter in plaintext:
        if letter in A:                                      # For each letter in the plaintext, replace the letter
            ciphertext += sub_alpha[(A.index(letter))]       # by the corresponding letter in the substitution alphabet.
        else:
            ciphertext += letter
    return ciphertext


def sub_decrypt(ciphertext, sub_alpha):
    plaintext = ""
    for letter in ciphertext:
        if letter in A:                                      # For each letter in the ciphertext, replace the
            plaintext += A[(sub_alpha.index(letter))]        # letter by the corresponding letter in the alphabet.
        else:
            plaintext += letter
    return plaintext


print(sub_encrypt("Hello World!", B))
print(sub_decrypt("eyssg vgksu!", B))
