from math import sqrt
from math import floor

def get_factors(num):

    factors = []

    limit = sqrt(num)

    k = 0

    while (True):


        for n in range(2, floor(limit)):

            if num % n == 0:
                factors.append([n, num/n])
                num = num/n
                break
        
        if len(factors) < k:
            print("Number of roots: ", k - 1)
            break

        k = k + 1

    return factors

if __name__ == '__main__':
    
    print(get_factors(210000))