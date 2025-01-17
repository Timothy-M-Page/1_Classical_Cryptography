import math
import random
from typing import Union

import numpy as np


alphabet = (' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]'
            '^_`abcdefghijklmnopqrstuvwxyz{|}~')


def hill_encrypt(plaintext: str, matrix: np.ndarray) -> str:
    if not isinstance(plaintext, str):
        raise TypeError(f'Plaintext must be a string.')
    if not isinstance(matrix, np.ndarray):
        raise TypeError(f'Matrix must be a numpy array.')

    dim = len(matrix)
    # Add random padding so the plaintext length is divisible by dimension.
    if len(plaintext) % dim > 0:
        for i in range(dim - (len(plaintext) % dim)):
            plaintext += alphabet[random.randint(0, len(alphabet)-1)]
    length = len(plaintext)
    # Transform each block of plaintext and append to the ciphertext.
    ciphertext = ''
    for block in range(length // dim):
        block1 = []
        for index in range(dim):
            block1.append(alphabet.index(plaintext[(block * dim) + index]))
        block2 = np.dot(matrix, block1)
        for transformed_index in block2:
            ciphertext += alphabet[transformed_index % len(alphabet)]
    return ciphertext


def determinant(matrix: np.ndarray) -> int:
    if not isinstance(matrix, np.ndarray):
        raise TypeError(f'Matrix must be a numpy array.')

    det = np.linalg.det(matrix)
    # Avoid floating point precision errors.
    if math.isclose(det, round(det)):
        return round(det)
    else:
        return det


def adjugate(matrix: np.ndarray) -> np.ndarray:
    if not isinstance(matrix, np.ndarray):
        raise TypeError(f'Matrix must be a numpy array.')

    rows, cols = matrix.shape
    cofactor_matrix = np.zeros_like(matrix, dtype=float)
    for i in range(rows):
        for j in range(cols):
            minor_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactor_matrix[i, j] = (-1)**(i+j) * determinant(minor_matrix)
    return np.transpose(cofactor_matrix)


def mod_matrix_inverse(matrix: np.ndarray, mod: int) -> Union[np.ndarray, str]:

    if not isinstance(matrix, np.ndarray):
        raise TypeError(f'Matrix must be a numpy array.')
    if not isinstance(mod, int):
        raise TypeError(f'mod must be an integer.')

    det = determinant(matrix)
    if det == 0:
        raise ValueError('Matrix determinant is zero.')
    det = det % mod
    if det == 0:
        raise ValueError(f'Matrix determinant is zero mod {mod}.')
    if math.gcd(det, mod) != 1:
        raise ValueError('Determinant must be coprime with modulus')

    mod_det_inv = pow(det, -1, mod)
    adj = adjugate(matrix)
    inv_matrix = (mod_det_inv * adj) % mod
    return inv_matrix.astype(int)


def hill_decrypt(ciphertext: str, matrix: np.ndarray) -> str:
    det = int(np.linalg.det(matrix))

    if not isinstance(ciphertext, str):
        raise TypeError(f'Ciphertext must be a string.')
    if not isinstance(matrix, np.ndarray):
        raise TypeError(f'Matrix must be a numpy array.')
    if np.gcd(det, len(alphabet)) != 1:
        raise ValueError(f'No inverse matrix, as gcd(det, len(alphabet)) > 1.')

    dim = len(matrix)
    length = len(ciphertext)
    inverse_matrix = mod_matrix_inverse(matrix, len(alphabet))
    # Same algorithm as for encryption using the inverse matrix.
    plaintext = ''
    for block in range(length // dim):
        block2 = []
        for index in range(dim):
            block2.append(alphabet.index(ciphertext[(block * dim) + index]))
        block1 = np.dot(inverse_matrix, block2)
        for transformed_index in block1:
            plaintext += alphabet[transformed_index % len(alphabet)]
    return plaintext
