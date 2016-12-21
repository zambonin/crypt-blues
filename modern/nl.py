#!/usr/bin/env python
# -*- coding: utf-8 -*-

sbox = {
    '0000': '1000', '0001': '0100', '0010': '0010', '0011': '0001',
    '0100': '1100', '0101': '0110', '0110': '0011', '0111': '1101',
    '1000': '1010', '1001': '0101', '1010': '1110', '1011': '0111',
    '1100': '1111', '1101': '1011', '1110': '1001', '1111': '0000'
}


def bin_to_str(num):
    return '{0:04b}'.format(num)


def multi_xor(arg1, arg2):
    result = 0
    for i in range(len(arg2)):
        if int(arg2[i]) == 1:
            result = result ^ int(arg1[i])
    return result


nl = []
for input_sum in range(16):
    row = []
    for output_sum in range(16):
        count = 0
        for key in list(sbox.keys()):
            if multi_xor(bin_to_str(input_sum), key) ^ \
               multi_xor(bin_to_str(output_sum), sbox[key]) == 0:
                count += 1
        row.append(count)
    nl.append(row)
