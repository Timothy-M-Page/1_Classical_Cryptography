

A = "abcdefghijklmnopqrstuvwxyz"


def atbash(plaintext):
    plaintext = plaintext.lower()
    ciphertext = ""
    for letter in plaintext:
        if letter in A:                                # For each letter in the plaintext replace the
            ciphertext += A[25 - A.index(letter)]      # letter by its reflection in the alphabet.
        else:
            ciphertext += letter
    return ciphertext


print(atbash("Hello World!"))
print(atbash("svool dliow!"))


# The atbash cipher is its own inverse.
