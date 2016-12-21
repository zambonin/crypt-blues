#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SPN():
    def __init__(self, permut, sbox):
        self.permut = permut
        self.sbox = sbox

    def encode(self, text, key):
        assert len(key) == 32 and len(text) == 16
        subkeys = self.gen_subkeys(key)

        for r in range(len(subkeys) - 1):
            before_sbox = ''
            for i in range(len(text)):
                before_sbox += self.xor(text[i], subkeys[r][i])

            subtext = []
            for i in range(0, len(before_sbox), 4):
                subtext.append(before_sbox[i:i + 4])

            after_sbox = ''
            for i in range(len(subtext)):
                subtext[i] = self.sbox[subtext[i]]
                after_sbox += subtext[i]

            if r < 3:
                text = ''
                for i in range(len(after_sbox)):
                    text += after_sbox[self.permut[i + 1] - 1]

        output = ''
        for i in range(len(after_sbox)):
            output += self.xor(after_sbox[i], subkeys[4][i])

        return output

    def gen_subkeys(self, key):
        key += key
        subkeys = []
        for i in range(1, 6):
            pos = (4 * i - 1) - 3
            subkeys.append(key[pos:pos + 16])
        return subkeys

    def xor(self, arg1, arg2):
        return str(int(arg1) ^ int(arg2))
