
def gcd_recursive(a, b):

    if a % b == 0:
        return b

    return gcd_recursive(b, a % b)

def gcd_iter(a, b):
    
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

if __name__ == '__main__':
    print(egcd(7, 9))
