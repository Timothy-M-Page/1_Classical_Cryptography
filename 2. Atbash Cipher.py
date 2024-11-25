

A = "abcdefghijklmnopqrstuvwxyz"

def Atbash(p):
    p = p.lower()
    c = ""
    for l in p:
        if l in A:                    # For each alphabetic character in the plaintext
            c += A[25 - A.index(l)]   # replace the character by its reflection in the string A.
        else:
            c += l
    return c

# Note that the Atbash cipher is its own inverse.
# Hence, there is no need for separate encryption and decryption functions.

print(Atbash("Hello World!"))
print(Atbash("svool dliow!"))
