

A = "abcdefghijklmnopqrstuvwxyz"

def caesar_encrypt(p,key):
    c = ""
    p = p.lower()
    for l in p:
        if l in A:                              # For each alphabetic character l in the plaintext
            c += A[(A.index(l) + key) % 26]     # shift the character key places in the alphabet.
        else:
            c += l
    return c

def caesar_decrypt(c,key):
    p = ""
    for l in c:
        if l in A:
            p += A[(A.index(l) - key) % 26]    # Shift the alphabetic characters back by key places.
        else:
            p += l
    return p


print(caesar_encrypt("Hello World!",10))
print(caesar_decrypt("rovvy gybvn!",10))


