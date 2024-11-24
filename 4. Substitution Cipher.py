

A = "abcdefghijklmnopqrstuvwxyz"
B = "poiuytrewqasdfghjklmnbvcxz"    # The substitution alphabet

def sub_encrypt(p, sub):            # 'sub' denotes the substitution alphabet.
    c = ""
    p = p.lower()
    for l in p:
        if l in A:                  # For each alphabetic character l in the plaintext, replace
            c += sub[(A.index(l))]  # the letter by the corresponding letter in the substitution alphabet.
        else:
            c += l
    return c

def sub_decrypt(c, sub):
    p = ""
    for l in c:
        if l in A:                  # For each alphabetic character l in the ciphertext, replace
            p += A[(sub.index(l))]  # the letter by the corresponding letter in the alphabet.
        else:
            p += l
    return p

print(sub_encrypt("Hello World!", B))
print(sub_decrypt("eyssg vgksu!", B))
