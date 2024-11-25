A = "abcdefghijklmnopqrstuvwxyz"

def vigenere_encrypt(p,key):
    p = p.lower()
    c = ""
    i = 0
    for l in p:                     # For each alphabetic character l in the plaintext
        if l in A:
            a = A.index(l)
            b = key[i % len(key)]   # Take the character of the key
            d = A.index(b)          # corresponding to the character's position in the plaintext
            c += A[(a+d) % len(A)]  # shift the letter by this value through the alphabet.
            i += 1
        else:
            c += l
    return c

def vigenere_decrypt(c,key):
    p = ""
    i = 0
    for l in c:                     # For each alphabetic character l in the ciphertext
        if l in A:
            a = A.index(l)
            b = key[i % len(key)]
            d = A.index(b)
            p += A[(a-d) % len(A)]  # analogously shift the letter back through the alphabet by the same value.
            i += 1
        else:
            p += l
    return p

print(vigenere_encrypt("Hello world!","keyword"))
print(vigenere_decrypt("rijhc nrbpb!","keyword"))

