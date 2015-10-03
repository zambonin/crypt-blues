def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def extended_gcd(num1, num2):
        gcd, remainder = abs(num1), abs(num2)
        x, y, old_x, old_y = 1, 1, 0, 0
        while remainder:
            gcd, (quotient, remainder) = remainder, divmod(gcd, remainder)
            old_x, x = x - quotient*old_x, old_x
            old_y, y = y - quotient*old_y, old_y
        return gcd, x, y


def inv_mod(a, mod):
    g, x, y = extended_gcd(a, mod)
    return int(x % mod)


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def quad_mult(x, b, n):
    z = 1
    b = "{0:b}".format(b)
    for i in range(len(b)):
        z = z**2 % n
        if b[i] == '1':
            z = z*x % n
    return z
