import binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad


def add_padding(text, blocksize=64):
    pad_len = blocksize - (len(text) % blocksize)
    padding = '$' * pad_len
    return text + padding

def remove_padding(text, blocksize=64):
    counter = 0

    for c in text[::-1]:
        if c == '$':
            counter += 1
        else:
            break

    return text[:-counter]

def encrypt(plain_text, key):
    des = AES.new(key, AES.MODE_CBC)
    return des.encrypt(pad(plain_text, AES.block_size))

def decrypt(cipher_text, key):
    des = AES.new(key, AES.MODE_CBC)
    return des.decrypt(cipher_text)


if __name__ == '__main__':

    key = b'12345678'
    plain_text = b'This is the secret message we want to encrypt!'
    cipher_text = encrypt(plain_text, key)
    print(cipher_text)
    encrypted = binascii.hexlify(bytearray(cipher_text))
    print("Encrypted text: %s " % encrypted)
    decrypted = unpad(decrypt(cipher_text, key), AES.block_size)
    print("Decrypted text: %s " % decrypted)