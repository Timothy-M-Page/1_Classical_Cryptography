import os

alphabet = (' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]'
            '^_`abcdefghijklmnopqrstuvwxyz{|}~')


def one_time_pad_encrypt(plaintext: str, key: str):

    if not isinstance(plaintext, str):
        raise TypeError(f'Plaintext must be a string.')
    if not isinstance(key, str):
        raise TypeError(f'Key must be a string.')

    key_length = len(key)
    plaintext_length = len(plaintext)

    if plaintext_length != key_length:
        raise ValueError('Key length must match plaintext length.')

    ciphertext = ''
    index = 0
    for letter in plaintext:
        if letter in alphabet:
            a = alphabet.index(letter)
            b = alphabet.index(key[index])
            # Shift each letter by the corresponding key letter.
            ciphertext += alphabet[(a + b) % len(alphabet)]
            index += 1
        else:
            ciphertext += letter
    return ciphertext


def one_time_pad_decrypt(ciphertext: str, key: str):

    if not isinstance(ciphertext, str):
        raise TypeError(f'Ciphertext must be a string.')
    if not isinstance(key, str):
        raise TypeError(f'Key must be a string.')

    key_length = len(key)
    ciphertext_length = len(ciphertext)

    if ciphertext_length != key_length:
        raise ValueError('Key length must match ciphertext length.')

    plaintext = ''
    index = 0
    for letter in ciphertext:
        if letter in alphabet:
            a = alphabet.index(letter)
            b = alphabet.index(key[index])
            # Shift the letter back by the corresponding key letter.
            plaintext += alphabet[(a - b) % len(alphabet)]
            index += 1
        else:
            plaintext += letter
    return plaintext


def random_key(length: int):
    """
    A random key of given length may be generated using the operating
    system package to access hardware events, the randomness of which
    is cryptographically secure.
    """

    if not isinstance(length, int):
        raise TypeError('Key length must be an integer.')
    if length <= 0:
        raise ValueError('Key length must be a positive integer.')

    random_bytes = os.urandom(length)
    key = ''.join(alphabet[byte % len(alphabet)] for byte in random_bytes)
    return key
