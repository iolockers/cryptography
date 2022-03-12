
def modular_inverse(a, m):

    for inv in range(0, m):
        if (a * inv) % m == 1:
            return inv

    print('There is no modular inverse (a is not a coprime to m)')

if __name__ == '__main__':
    print(modular_inverse(91232131231, 31444444444446))