#!/usr/bin/env python

import string
import sys
from enigma import Enigma, Walzen

rotors=('I', 'II', 'III', 'IV', 'V')

def index_of_coincidence(text):
    def freq(i):
        c = text.count(i)
        return c * (c - 1)

    l = len(text)
    return sum(map(freq, string.ascii_uppercase)) / (l * (l - 1))

def main(text):
    for i in rotors:
        for j in rotors:
            if i == j:
                continue
            for k in rotors:
                if i == k or j == k:
                    continue
                for l in string.ascii_uppercase:
                    for m in string.ascii_uppercase:
                        for n in string.ascii_uppercase:
                            deciphered = Enigma(rotors=
                            (Walzen(index='%s' % i, ringstellung='A', grundstellung='%s' % l),
                             Walzen(index='%s' % j, ringstellung='A', grundstellung='%s' % m),
                             Walzen(index='%s' % k, ringstellung='A', grundstellung='%s' % n))).cipher(text)
                            yield ('(%s%s%s %s %s %s): %s' % (
                                l, m, n, i, j, k,
                                deciphered
                            ), index_of_coincidence(deciphered))

if __name__ == '__main__':
    ics = main(sys.argv[1])

    filtered_ics = filter(lambda v: 0.05 < v[1] <= 0.07, ics)

    sorted_ics = sorted(filtered_ics, key=lambda o: o[1], reverse=True)

    with open('result.out', 'w') as fp:
        for i in sorted_ics:
            fp.write(str(i))