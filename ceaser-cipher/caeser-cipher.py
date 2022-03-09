ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 5

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

    plain_text = "Testando se este texto esta em portugues Serao aprovados textos que contenham pelo menos setenta porcento ou mais em portugues"
    encrypted = ceaser_encrypt(plain_text)
    print(encrypted)
    print(ceaser_decrypt(encrypted))