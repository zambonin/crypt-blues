#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint, shuffle
from spn import SPN

key = '{0:032b}'.format(randint(0, 2**32))
permut = {
    1: 1, 2: 5, 3: 9, 4: 13, 5: 2, 6: 6, 7: 10, 8: 14, 9: 3,
    10: 7, 11: 11, 12: 15, 13: 4, 14: 8, 15: 12, 16: 16,
}
sbox = {
    '0000': '1000', '0001': '0100', '0010': '0010', '0011': '0001',
    '0100': '1100', '0101': '0110', '0110': '0011', '0111': '1101',
    '1000': '1010', '1001': '0101', '1010': '1110', '1011': '0111',
    '1100': '1111', '1101': '1011', '1110': '1001', '1111': '0000',
}
inverse_sbox = {v: k for k, v in sbox.items()}
_spn = SPN(permut, sbox)


def gen_pairs(k, range_):
    seq = list(range(2**16))
    shuffle(seq)
    pairs = []

    for i in seq[:range_]:
        i = '{0:016b}'.format(i)
        pairs += [[i, _spn.encode(i, key)]]
    return pairs


count = [[0 for i in range(16)] for j in range(16)]

for pair in gen_pairs(key, 1500):
    for i in range(16):
        for j in range(16):
            v4_1 = i ^ int(pair[1][0:4], 2)
            v4_3 = j ^ int(pair[1][8:12], 2)
            u4_1 = inverse_sbox['{0:04b}'.format(v4_1)]
            u4_3 = inverse_sbox['{0:04b}'.format(v4_3)]
            z = int(pair[0][-1]) ^ int(u4_1[0]) ^ int(u4_3[0])
            if z == 0:
                count[i][j] += 1

subkey = _spn.gen_subkeys(key)[4]
print("subkey:\t{} {}".format(subkey[:4], subkey[8:12]))
_max = max(map(max, count))
for n, l in enumerate(count):
    try:
        print("guess:\t{0:04b} {0:04b}".format(n, l.index(_max)))
    except:
        pass
