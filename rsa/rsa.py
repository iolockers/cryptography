import random
from math import floor
from math import sqrt

RANDOM_START = 1e3
RANDOM_END = 1e5

def is_prime(num):

    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for n in range(3, floor(sqrt(num))+1, 2):
        if num % n == 0:
            return False

    return True

def gcd(a, b):
    
    while a % b != 0:
        a, b = b, a % b

    return b

def egcd(a, b):

    if a == 0:
        return b, 0 , 1
    
    gcd, x1, y1 = egcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def generate_large_prime(start=RANDOM_START, end=RANDOM_END):
    num = random.randint(start, end)

    while not is_prime(num):
        num = random.randint(start, end)

    return num

def generate_rsa_keys():
    p = generate_large_prime()
    q = generate_large_prime()

    n = p * q
    phi = (p-1)*(q-1)
    e = random.randrange(1, phi)

    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = egcd(e, phi)[1]

    return (d, n), (e, n)

def encrypt(public_key, plain_text):
    
    e, n = public_key

    cipher_text = []

    for char in plain_text:
        a = ord(char)
        cipher_text.append(pow(a, e, n))

    return cipher_text

def decrypt(private_key, cipher_text):

    d, n = private_key

    plain_text = ''

    for num in cipher_text:
        a = pow(num, d, n)
        plain_text = plain_text + str(chr(a))

    return plain_text


if __name__ == '__main__':
    private_key, public_key = generate_rsa_keys()

    message = 'eu estou olhando vários prédios na avenida silva jardim'

    print("Public Key:", public_key, "| Private Key:", private_key)

    cipher = encrypt(public_key, message)
    print(cipher)

    plain = decrypt(private_key, cipher)
    print(plain)

