#!/usr/bin/env python

import pprint
import string
import sys

allowed_letters = string.ascii_lowercase
digraph_index = {}
letter_index = {l: 0 for l in allowed_letters}


def process_text(text):
    for word in text.lower().split():
        if len(word) > 1:
            digraphs = tuple(word[x:x + 2] for x in range(len(word) - 1))
            for dig in digraphs:
                if dig[0] in allowed_letters and dig[1] in allowed_letters:
                    letter_index[dig[0]] += 1
                    digraph_index[dig] = digraph_index[dig] + 1 \
                        if dig in digraph_index else 1

        if word[-1] in allowed_letters:
            letter_index[word[-1]] += 1


def process_data():
    total = sum(digraph_index.values())

    for let in letter_index:
        letter_index[let] /= total

    for dig in digraph_index:
        digraph_index[dig] /= total

    return sorted(letter_index.items(), key=lambda o: o[1], reverse=True), \
        sorted(digraph_index.items(), key=lambda o: o[1], reverse=True)[:10]

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        with open(arg) as raw:
            for line in raw:
                process_text(line)

    pprint.pprint(process_data())
