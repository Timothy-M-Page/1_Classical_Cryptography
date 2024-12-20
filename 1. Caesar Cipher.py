

A = "abcdefghijklmnopqrstuvwxyz"


def caesar_encrypt(plaintext, key):
    ciphertext = ""
    plaintext = plaintext.lower()
    for letter in plaintext:
        if letter in A:                                       # For each letter in the plaintext shift
            ciphertext += A[(A.index(letter) + key) % 26]     # the letter 'key' places through the alphabet.
        else:
            ciphertext += letter
    return ciphertext


def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        if letter in A:
            plaintext += A[(A.index(letter) - key) % 26]      # Shift the letter back by 'key' places.
        else:
            plaintext += letter
    return plaintext


print(caesar_encrypt("Hello World!", 10))
print(caesar_decrypt("rovvy gybvn!", 10))

