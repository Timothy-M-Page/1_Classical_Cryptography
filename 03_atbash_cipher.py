alphabet = 'abcdefghijklmnopqrstuvwxyz'


def atbash(plaintext: str) -> str:

    if not isinstance(plaintext, str):
        raise TypeError(f'Plaintext must be a string.')

    ciphertext = ''
    plaintext = plaintext.lower()
    for letter in plaintext:
        if letter in alphabet:
            # Replace each letter by its reflection in the alphabet.
            ciphertext += alphabet[25 - alphabet.index(letter)]
        else:
            ciphertext += letter
    return ciphertext
