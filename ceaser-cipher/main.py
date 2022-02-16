ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
KEY = 3

def ceaser_encrypt(plain_text):

    cipher_text = ''
    plain_text = plain_text.upper()

    for c in plain_text:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]
    
    return cipher_text

def ceaser_decrypt(cipher_text):

    plain_text = ''

    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]
    
    return plain_text


if __name__ == '__main__':

    m = 'Welcome to my Udemy course'
    encrypted = ceaser_encrypt(m)
    print(encrypted)
    print(ceaser_decrypt(encrypted))