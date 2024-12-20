import math
import numpy as np
import random


A = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def hill_encrypt(plaintext, matrix):
    dim = len(matrix)
    if len(plaintext) % dim > 0:
        for i in range(dim - (len(plaintext) % dim)):           # Add random padding to ensure the plaintext is
            plaintext += A[random.randint(0, len(A)-1)]        # a multiple of the dimension of the matrix.
    length = len(plaintext)
    ciphertext = ""
    for i in range(length // dim):                              # i ranges over blocks of the plaintext of length dim.
        block1 = []
        for j in range(dim):
            block1.append(A.index(plaintext[(i * dim) + j]))    # block1 is the i-th block of plaintext.
        block2 = np.dot(matrix, block1)                         # block2 is block1 transformed by the matrix.
        for x in block2:
            ciphertext += A[x % len(A)]
    return ciphertext


def det(matrix):
    determinant = np.linalg.det(matrix)
    if math.isclose(determinant, round(determinant)):   # Avoid floating point precision errors.
        return round(determinant)
    else:
        return determinant


def adjugate(matrix):            # The adjugate matrix is used for calculating the inverse matrix.
    rows, cols = matrix.shape
    cofactor_matrix = np.zeros_like(matrix, dtype=float)
    for i in range(rows):
        for j in range(cols):
            minor_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactor_matrix[i, j] = ((-1) ** (i + j)) * det(minor_matrix)
    return np.transpose(cofactor_matrix)


def modular_matrix_inverse(matrix, mod):
    try:
        matrix = np.array(matrix)
        det_matrix = det(matrix) % mod
        if det_matrix == 0:
            return "Matrix determinant is zero mod " + str(mod)
        det_inv = pow(det_matrix, -1, mod)
        adj = adjugate(matrix)
        inv_matrix = (det_inv * adj) % mod
        return inv_matrix.astype(int)
    except ValueError:
        return "Determinant is not invertible modulo " + str(mod) + "."
    except np.linalg.LinAlgError:
        return "Matrix is singular."


def hill_decrypt(ciphertext, matrix):
    dim = len(matrix)
    length = len(ciphertext)
    determinant = int(np.linalg.det(matrix))
    if np.gcd(determinant, len(A)) != 1:
        print("Inverse matrix not computable due to gcd(det, len(A)) > 1.")  # Error message for un-invertible matrices.
        return ""
    inverse_matrix = modular_matrix_inverse(matrix, len(A))
    plaintext = ""
    for i in range(length // dim):
        block2 = []
        for j in range(dim):
            block2.append(A.index(ciphertext[(i * dim) + j]))
        block1 = np.dot(inverse_matrix, block2)                    # Same algorithm as for encryption, only using the
        for x in block1:                                           # inverse matrix, instead of the original matrix.
            plaintext += A[x % len(A)]
    return plaintext


print(hill_encrypt("Hello World!",[[5,1],[3,4]]))
print(hill_decrypt("o0lY/Oe&+kX2",[[5,1],[3,4]]))



