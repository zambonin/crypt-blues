#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enigma import Enigma, Walzen
from itertools import permutations, product
from sys import argv

rotors = ('I', 'II', 'III', 'IV', 'V')
_upper = list(map(chr, range(65, 91)))
rot_comb = list(permutations(rotors, 3))
let_prod = list(product(_upper, repeat=3))


def index_of_coincidence(text):
    def freq(i):
        c = text.count(i)
        return c * (c - 1)

    l = len(text)
    return sum(map(freq, _upper)) / (l * (l - 1))


def test_rotors(text):
    for i, j, k in rot_comb:
        for l, m, n in let_prod:
            deciphered = Enigma(rotors=(
                Walzen(index=i, ringstellung='A', grundstellung=l),
                Walzen(index=j, ringstellung='A', grundstellung=m),
                Walzen(index=k, ringstellung='A', grundstellung=n)
            )).cipher(text)
            yield ('(%s%s%s %s %s %s): %s' % (l, m, n, i, j, k, deciphered),
                   index_of_coincidence(deciphered))


if __name__ == '__main__':

    if len(argv) == 2:
        ics = test_rotors(argv[1])
        filtered_ics = filter(lambda v: 0.05 < v[1] <= 0.07, ics)
        sorted_ics = sorted(filtered_ics, key=lambda o: o[1], reverse=True)

        with open('result.out', 'w') as fp:
            for i in sorted_ics:
                fp.write(str(i))
