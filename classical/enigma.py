#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

alphabet = list(map(chr, range(65, 91)))
desloc = alphabet[1:] + alphabet[:1]
shift_up = {alphabet[i]: desloc[i] for i in range(len(alphabet))}


class Steckerbrett:
    def __init__(self, *args):
        self.map = {}

        for arg in args:
            if arg[0] in self.map or arg[1] in self.map:
                raise KeyError('Same letter used twice in plugboard')

            self.map[arg[0]] = arg[1]
            self.map[arg[1]] = arg[0]

    def swap(self, letter):
        if letter in self.map:
            return self.map[letter]
        return letter


class Umkehrwalze:
    def __init__(self, wiring):
        assert isinstance(wiring, str)
        self.wiring = wiring

    def reflect(self, letter):
        return self.wiring[alphabet.index(letter)]


class Walzen:
    def __init__(self, index, grundstellung, ringstellung):
        if index == 'I':
            self.wiring = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
            self.notch = 'Q'
        elif index == 'II':
            self.wiring = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
            self.notch = 'E'
        elif index == 'III':
            self.wiring = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
            self.notch = 'V'
        elif index == 'IV':
            self.wiring = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
            self.notch = 'J'
        elif index == 'V':
            self.wiring = 'VZBRGITYUPSDNHLXAWMJQOFECK'
            self.notch = 'Z'

        if isinstance(self.notch, str) and len(self.notch) == 1:
            self.notch = alphabet.index(self.notch)

        if isinstance(ringstellung, str) and len(ringstellung) == 1:
            self.ringstellung = alphabet.index(ringstellung)

        if isinstance(grundstellung, str) and len(grundstellung) == 1:
            self.grundstellung = alphabet.index(grundstellung)

    def wire(self, forward):
        permut = {}
        for i in range(len(self.wiring)):
            permut[alphabet[i]] = self.wiring[i]
        if not forward:
            return {v: k for k, v in permut.items()}
        return permut

    def move(self, char, steps, permutation):
        if steps < 0:
            permutation = {v: k for k, v in permutation.items()}
            steps *= -1
        for i in range(steps):
            char = permutation[char]
        return char


class Enigma:
    def __init__(self, rotors, plugboard=None):
        assert plugboard is None or isinstance(plugboard, Steckerbrett)

        assert isinstance(rotors, tuple)
        for index in range(len(rotors)):
            assert isinstance(rotors[index], Walzen)

        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = Umkehrwalze(wiring='YRUHQSLDPXNGOKMIEBFZCWVJAT')

    def cipher(self, message):
        assert isinstance(message, str)

        message = message.upper()
        ciphered = ''

        p1 = self.rotors[0].grundstellung
        p2 = self.rotors[1].grundstellung
        p3 = self.rotors[2].grundstellung

        n1 = self.rotors[0].notch
        n2 = self.rotors[1].notch

        r1 = self.rotors[0].ringstellung
        r2 = self.rotors[1].ringstellung
        r3 = self.rotors[2].ringstellung

        m1 = (n1 - p1) % 26
        m2 = m1 + 26 * ((n2 - p2 - 1) % 26) + 1

        i1 = p1 - r1 + 1

        for j in range(len(message)):
            letter = message[j]

            k1 = int((j - m1 + 26) / 26)
            k2 = int((j - m2 + 650) / 650)

            i2 = p2 - r2 + k1 + k2
            i3 = p3 - r3 + k2

            letter = self.rotors[0].move(letter, i1 + j, shift_up)
            letter = self.rotors[0].move(letter, 1, self.rotors[0].wire(True))
            letter = self.rotors[0].move(letter, -i1 - j, shift_up)
            letter = self.rotors[1].move(letter, i2, shift_up)
            letter = self.rotors[1].move(letter, 1, self.rotors[1].wire(True))
            letter = self.rotors[1].move(letter, -i2, shift_up)
            letter = self.rotors[2].move(letter, i3, shift_up)
            letter = self.rotors[2].move(letter, 1, self.rotors[2].wire(True))
            letter = self.rotors[2].move(letter, -i3, shift_up)
            letter = self.reflector.reflect(letter)
            letter = self.rotors[2].move(letter, i3, shift_up)
            letter = self.rotors[2].move(letter, 1, self.rotors[2].wire(False))
            letter = self.rotors[2].move(letter, -i3, shift_up)
            letter = self.rotors[1].move(letter, i2, shift_up)
            letter = self.rotors[1].move(letter, 1, self.rotors[1].wire(False))
            letter = self.rotors[1].move(letter, -i2, shift_up)
            letter = self.rotors[0].move(letter, i1 + j, shift_up)
            letter = self.rotors[0].move(letter, 1, self.rotors[0].wire(False))
            letter = self.rotors[0].move(letter, -i1 - j, shift_up)

            ciphered += letter

        return ciphered


if __name__ == '__main__':
    # INSERT FROM RIGHT TO LEFT LIKE NORMAL ENIGMA
    rotors = (Walzen(index='I', grundstellung='C', ringstellung='A'),
              Walzen(index='II', grundstellung='S', ringstellung='A'),
              Walzen(index='III', grundstellung='F', ringstellung='A'))

    if len(argv) == 2:
        print(Enigma(rotors=rotors).cipher(argv[1]))
