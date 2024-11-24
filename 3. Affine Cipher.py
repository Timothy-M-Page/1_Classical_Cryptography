
A = "abcdefghijklmnopqrstuvwxyz"

def inv(a):                             # Inverse element in the group Z/26Z
    for x in range(1,26):
        if a*x % 26 == 1:
            return x
    print(f"{a} has no inverse mod 26")  # Error message if gcd(a,26) > 1.
    return None

def affine_encrypt(a,b,p):                         # a and b represent the integers used in the affine cipher.
    c = ""
    p = p.lower()
    for l in p:
        if l in A:                                  # For each alphabetic character l in the plaintext
            c += A[(b + (a*A.index(l))) % 26]       # replace the letter by a*l + b mod 26.
        else:
            c += l
    return c

def affine_decrypt(a,b,c):
    p = ""
    x = inv(a)
    if x is None:
        return "Decryption failed due to no inverse."
    for l in c:
        if l in A:                                  # For each alphabetic character l in the ciphertext
            p += A[((A.index(l) - b) * x) % 26]     # replace the letter by (l-b)*inv(a) mod 26.
        else:
            p += l
    return p


print(affine_encrypt(3,4,"Hello World!"))
print(affine_decrypt(3,4,"zqllu sudln!"))


