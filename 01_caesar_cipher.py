alphabet = 'abcdefghijklmnopqrstuvwxyz'


def caesar_encrypt(plaintext: str, key: int) -> str:
    if not isinstance(plaintext, str):
        raise TypeError(f'Plaintext must be a string.')
    if not isinstance(key, int):
        raise TypeError(f'Key must be an integer.')
    plaintext = plaintext.lower()
    ciphertext = ''
    for letter in plaintext:
        if letter in alphabet:
            # Shift each letter by 'key' places.
            ciphertext += alphabet[(alphabet.index(letter) + key)
                                   % len(alphabet)]
        else:
            ciphertext += letter
    return ciphertext


def caesar_decrypt(ciphertext: str, key: int) -> str:
    if not isinstance(ciphertext, str):
        raise TypeError(f'Ciphertext must be a string.')
    if not isinstance(key, int):
        raise TypeError(f'Key must be an integer.')
    plaintext = ''
    for letter in ciphertext:
        if letter in alphabet:
            # Shift the letter back by 'key' places.
            plaintext += alphabet[(alphabet.index(letter) - key)
                                  % len(alphabet)]
        else:
            plaintext += letter
    return plaintext
