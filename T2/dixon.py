import utils

def factor(n=256961):
    base = [-1] + [x for x in range(2, 32) if utils.is_prime(x)]
    start = int(n ** .5)
    pairs, factors = [], []

    for i in range(start, n):
        for j in base:
            if i**2 % n == j**2 % n: 
                pairs.append([i,j])

    for i in pairs:
        factor = utils.gcd(i[0] - i[1], n)
        if factor != 1:
            return (factor, int(n/factor))