from typing import Optional

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def mod_inv(a: int) -> Optional[int]:
    # Inverse element in the group Z/len(alphabet)Z.
    mod = len(alphabet)
    for x in range(1, mod):
        if a*x % mod == 1:
            return x
    return None


def affine_encrypt(plaintext: str, a: int, b: int) -> str:

    if not isinstance(plaintext, str):
        raise TypeError(f'Plaintext must be a string.')
    if not isinstance(a, int):
        raise TypeError(f'a must be an integer.')
    if not isinstance(b, int):
        raise TypeError(f'b must be an integer.')

    ciphertext = ''
    plaintext = plaintext.lower()
    for letter in plaintext:
        if letter in alphabet:
            # Replace each letter by (a * letter.index) + b mod len(alphabet).
            index = alphabet.index(letter)
            ciphertext += alphabet[(b + (a * index)) % len(alphabet)]
        else:
            ciphertext += letter
    return ciphertext


def affine_decrypt(ciphertext: str, a: int, b: int) -> str:

    if not isinstance(ciphertext, str):
        raise TypeError(f'Ciphertext must be a string.')
    if not isinstance(a, int):
        raise TypeError(f'a must be an integer.')
    if not isinstance(b, int):
        raise TypeError(f'b must be an integer.')

    plaintext = ''
    inv = mod_inv(a)
    if inv is None:
        raise ValueError(f'Decryption failed due to no inverse for {a}.')

    for letter in ciphertext:
        if letter in alphabet:
            # Replace each letter by (letter.index - b) * mod_inv(a)
            index = alphabet.index(letter)
            plaintext += alphabet[((index - b) * inv) % len(alphabet)]
        else:
            plaintext += letter
    return plaintext
