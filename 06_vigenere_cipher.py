alphabet = (' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]'
            '^_`abcdefghijklmnopqrstuvwxyz{|}~')


def vigenere_encrypt(plaintext: str, key: str) -> str:

    if not isinstance(plaintext, str):
        raise TypeError(f'Plaintext must be a string.')
    if not isinstance(key, str) or not key:
        raise TypeError(f'Key must be a non-empty string.')

    plaintext = plaintext.lower()
    ciphertext = ''
    index = 0
    for letter in plaintext:
        if letter in alphabet:
            a = alphabet.index(letter)
            b = alphabet.index(key[index % len(key)])
            # Shift each letter by the corresponding key letter.
            ciphertext += alphabet[(a+b) % len(alphabet)]
            index += 1
        else:
            ciphertext += letter
    return ciphertext


def vigenere_decrypt(ciphertext: str, key: str) -> str:

    if not isinstance(ciphertext, str):
        raise TypeError(f'Ciphertext must be a string.')
    if not isinstance(key, str) or not key:
        raise TypeError(f'Key must be a non-empty string.')

    plaintext = ''
    index = 0
    for letter in ciphertext:
        if letter in alphabet:
            a = alphabet.index(letter)
            b = alphabet.index(key[index % len(key)])
            # Shift the letter back by the corresponding key letter.
            plaintext += alphabet[(a-b) % len(alphabet)]
            index += 1
        else:
            plaintext += letter
    return plaintext
