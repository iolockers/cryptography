from math import sqrt
from math import floor
import random

def is_prime_naive(num):

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


def is_prime(n, k=10):

    if n <= 1:
        return False

    for _ in range(k):

        a = random.randint(2, n) - 1

        if pow(a, n-1, n) != 1:
            return False

    return True


if __name__ == '__main__':

    print(is_prime(99194853094755497))
