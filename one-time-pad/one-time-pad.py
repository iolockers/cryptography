from random import randint

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text, key):
    text = text.upper()
    cipher_text = ''

    for index, char in enumerate(text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]

    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ''

    for index, char in enumerate(cipher_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain_text += ALPHABET[(char_index - key_index) % len(ALPHABET)]

    return plain_text


def random_sequence(text):
    random = []

    for _ in range(len(text)):
        random.append(randint(0,len(ALPHABET)-1))

    return random

if __name__ == '__main__':
    message = 'this is a sample text that will be encrypted by one time pad and then decrypted to check the result'
    seq = random_sequence(message)
    print("Original message: %s" % message.upper())
    encrypted = encrypt(message, seq)
    print("Encrypted message: %s" % encrypted)
    decrypted = decrypt(encrypted, seq)
    print("Decrypted message: %s" % decrypted)

