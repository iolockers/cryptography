import random

def generate_private_key(n, g):

    x = random.randint(1, n)
    y = random.randint(1, n)

    k1 = pow(g, x, n)
    k2 = pow(g, y, n)

    print("Key 1 %s" % (pow(k2, x, n)))
    print("Key 2 %s" % (pow(k1, y, n)))


if __name__ == '__main__':
    
    n = 37
    g = 13

    generate_private_key(n, g)
