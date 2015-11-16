`q1_freq.py` will open any number of files given through arguments and print
the sorted distribution of letter and digram frequencies.

```
chmod u+x q1_freq.py
./q1_freq.py foo.in bar.in
```

A free copy of Victor Hugo's _Les Miserábles_ is included for testing purposes.

`q3_enigma.py` is a simple Enigma M3 implementation that doesn't consider a
_Steckerbrett_ for debugging purposes. It's also lacking different component
models such as rotors and reflectors. `q3_enig_breaker.py` will break a
cyphered text that's long enough through a index of coincidence test.

```
chmod u+x q3_enigma.py
./q3_enigma.py FOOBARTEXTTOENCODE
```

`q4_spn.py` is a simple SPN (substitution-permutation network) implementation
that will encode any given 16-bit text with a 32-bit key. `q4_break_spn.py` is
a probabilistic differential attack that will try to find, through differential
trails, the right subkey for the given information. It's a functional
representation of Douglas Stinson's _Cryptography: Theory and Practice_
differential attack, 2nd edition, p. 94.

They are **not** guaranteed to be fast.
