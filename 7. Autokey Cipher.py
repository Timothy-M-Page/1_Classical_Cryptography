

A = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def autokey_encrypt(plaintext, key):
    key2 = key + plaintext                      # Adjoin the plaintext to the key to form key2.
    ciphertext = ""
    i = 0
    for letter in plaintext:
        if letter in A:
            a = A.index(letter)                 # Letter's index in the alphabet.
            b = key2[i]                         # Corresponding character in the key.
            d = A.index(b)                      # Key character's index in the alphabet.
            ciphertext += A[(a+d) % len(A)]     # Shift the letter by the character's index.
            i += 1
        else:
            ciphertext += letter
    return ciphertext


def autokey_decrypt(ciphertext, key):
    key2 = key
    plaintext = ""
    i = 0
    for letter in ciphertext:
        if letter in A:
            a = A.index(letter)
            b = key2[i]
            d = A.index(b)
            plaintext += A[(a-d) % len(A)]      # Shift the letter back through the alphabet by the same value.
            key2 += plaintext[i]                # For each decrypted letter of the plaintext, reconstruct the
            i += 1                              # original key2 by iteratively adding each decrypted letter.
        else:
            plaintext += letter
    return plaintext


print(autokey_encrypt("Hello World!", "keyword"))
print(autokey_decrypt("4Kfd_r<8XYQp", "keyword"))


