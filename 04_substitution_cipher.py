alphabet = 'abcdefghijklmnopqrstuvwxyz'
substitution_alphabet = 'poiuytrewqasdfghjklmnbvcxz'


def sub_encrypt(plaintext: str, sub_alpha: str) -> str:

    if not isinstance(plaintext, str):
        raise TypeError(f'Plaintext must be a string.')
    if not isinstance(sub_alpha, str):
        raise TypeError(f'Substitution alphabet must be a string.')
    if set(alphabet) != set(sub_alpha):
        raise ValueError(
            'Substitution alphabet must be a permutation of the alphabet.')

    plaintext = plaintext.lower()
    ciphertext = ''
    for letter in plaintext:
        if letter in alphabet:
            # Replace each letter by the corresponding letter in sub_alpha.
            ciphertext += sub_alpha[(alphabet.index(letter))]
        else:
            ciphertext += letter
    return ciphertext


def sub_decrypt(ciphertext: str, sub_alpha: str) -> str:

    if not isinstance(ciphertext, str):
        raise TypeError(f'Ciphertext must be a string.')
    if not isinstance(sub_alpha, str):
        raise TypeError(f'Substitution alphabet must be a string.')
    if set(alphabet) != set(sub_alpha):
        raise ValueError(
            'Substitution alphabet must be a permutation of the alphabet.')

    plaintext = ''
    for letter in ciphertext:
        if letter in alphabet:
            # Replace each letter by the corresponding letter in the alphabet.
            plaintext += alphabet[(sub_alpha.index(letter))]
        else:
            plaintext += letter
    return plaintext
