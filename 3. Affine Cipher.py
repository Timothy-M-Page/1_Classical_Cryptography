

A = "abcdefghijklmnopqrstuvwxyz"


def inv_mod26(a):                            # Inverse element in the group Z/26Z.
    for x in range(1, 26):
        if a*x % 26 == 1:
            return x
    return f'{a} has no inverse mod 26'      # Error message if there is no inverse due to gcd(a, 26) > 1.


def affine_encrypt(a, b, plaintext):          # a and b represent the integers used in the affine cipher.
    ciphertext = ""
    plaintext = plaintext.lower()
    for letter in plaintext:
        if letter in A:                                           # For each letter in the plaintext
            ciphertext += A[(b + (a*A.index(letter))) % 26]       # replace the letter by a*letter + b mod 26.
        else:
            ciphertext += letter
    return ciphertext


def affine_decrypt(a, b, ciphertext):
    plaintext = ""
    x = inv_mod26(a)
    if x is None:
        return "Decryption failed due to no inverse."
    for letter in ciphertext:
        if letter in A:                                           # For each letter in the ciphertext
            plaintext += A[((A.index(letter) - b) * x) % 26]      # replace the letter by (letter-b)*inv_mod26(a)
        else:                                                     # mod 26, to recover the original letter.
            plaintext += letter
    return plaintext


print(affine_encrypt(3, 4, "Hello World!"))
print(affine_decrypt(3, 4, "zqllu sudln!"))


