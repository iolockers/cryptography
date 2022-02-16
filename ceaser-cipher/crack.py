ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
KEY = 3

def crack_ceaser(cipher_text):

    for key in range(len(ALPHABET)):
        plain_text = ''

        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index] 

        print('With the %s key, the result is %s' % (key, plain_text))


if __name__ == '__main__':
    encrypted = "ZHOFRPHCWRCPACXGHPACFRXUVH"
    crack_ceaser(encrypted)