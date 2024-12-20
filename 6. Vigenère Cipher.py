

A = "abcdefghijklmnopqrstuvwxyz"


def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.lower()
    ciphertext = ""
    i = 0
    for letter in plaintext:
        if letter in A:
            a = A.index(letter)                 # Letter's index in the alphabet.
            b = key[i % len(key)]               # Corresponding character in the key.
            d = A.index(b)                      # Key character's index in the alphabet.
            ciphertext += A[(a+d) % len(A)]     # Shift the letter by the character's index.
            i += 1
        else:
            ciphertext += letter
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    i = 0
    for letter in ciphertext:
        if letter in A:
            a = A.index(letter)
            b = key[i % len(key)]
            d = A.index(b)
            plaintext += A[(a-d) % len(A)]      # Shift the letter back through the alphabet by the same value.
            i += 1
        else:
            plaintext += letter
    return plaintext


print(vigenere_encrypt("Hello World!", "keyword"))
print(vigenere_decrypt("rijhc nrbpb!", "keyword"))

