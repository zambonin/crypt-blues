import utils


def factor(n=618240007109027021):
    a = 2
    bound = int(n ** .5)

    for j in range(2, bound):
        a = a**j % n
        d = utils.gcd(a - 1, n)
        if 1 < d < n:
            return d
