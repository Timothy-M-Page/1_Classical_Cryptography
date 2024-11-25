
A = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def autokey_encrypt(p, key):
    key2 = key + p                    # Adjoin the plaintext to the key to form key2.
    c = ""
    i = 0
    for l in p:
        if l in A:                     # For each character l in the plaintext
            a = A.index(l)
            b = key2[i]                # Take the character of the key
            d = A.index(b)             # corresponding to the character's position in the plaintext
            c += A[(a+d) % len(A)]     # shift the letter by this value through the alphabet.
            i += 1
        else:
            c += l
    return c

def autokey_decrypt(c, key):
    key2 = key
    p = ""
    i = 0
    for l in c:
        if l in A:                     # For each alphabetic character l in the plaintext
            a = A.index(l)
            b = key2[i]
            d = A.index(b)
            p += A[(a-d) % len(A)]     # analogously shift the letter back through the alphabet by the same value.
            key2 += p[i]               # With each decrypted letter of the plaintext, reconstruct the original key2
            i += 1                     # by iteratively adding each decrypted letter.
        else:
            p += l
    return p


print(autokey_encrypt("Hello world!","keyword"))
print(autokey_decrypt("4Kfd_r\8XYQp","keyword"))


