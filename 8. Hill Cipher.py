import math
import numpy as np
import random

A = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def hill_encrypt(p,M):                              # M denotes the matrix used for encryption.
    p = p.lower()
    D = len(M)                                      # D denotes the dimension of the matrix.
    if len(p)%D > 0:
        for i in range(D - (len(p) % D)):           # Add random padding to ensure the plaintext is
            p += A[random.randint(0, len(A))]    # a multiple of the dimension of the matrix
    L = len(p)
    c = ""
    for i in range(L // D):                      # i ranges over blocks of the plaintext of length D
        C = []
        for j in range(D):
            C.append(A.index(p[(i * D) + j]))    # C is the i-th block of plaintext
        E = np.dot(M,C)                          # E is those elements in C transformed by the matrix A
        for x in E:                              # Here we use the numpy dot product.
            c += A[x % len(A)]
    return c


def det(matrix):
    det = np.linalg.det(matrix)
    if math.isclose(det, round(det)):   # Avoid floating point precision errors.
        return round(det)
    else:
        return det

def matrix_inverse(M):
    return np.linalg.inv(M)

def modular_matrix_inverse(A,mod):
    return np.round(matrix_inverse(A) * det(A) * pow(det(A),-1,mod)).astype(int) % mod


def hill_decrypt(c,M):
    D = len(M)
    L = len(c)
    det = int(np.linalg.det(M))
    if np.gcd(det, len(A)) != 1:
        print("Inverse matrix not computable due to gcd(det,len(A)) > 1.")  # Error message for un-invertable matrices.
        return ""
    I = modular_matrix_inverse(M,len(A))
    p = ""
    for i in range(L // D):
        C = []
        for j in range(D):
            C.append(A.index(c[(i * D) + j]))
        E = np.dot(I,C)                            # Same algorithm as for encryption, only using the inverse
        for x in E:                                # matrix I, instead of the original matrix M.
            p += A[x % len(A)]
    return p


print(hill_encrypt("Hello world!",[[5,1],[3,4]]))
print(hill_decrypt("Q1lY/OG'+kX2",[[5,1],[3,4]]))



