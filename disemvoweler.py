#!/usr/bin/env python

# my attempt at solving this problem

import sys

if len(sys.argv) != 2:
    print('Usage:')
    print('    ./disemvoweler.py "<input string>"')
    print('Example:')
    print('    ./disemvoweler.py "two drums and a cymbal fall off a cliff"')
    sys.exit()

input_str = sys.argv[1]

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

outC = ''
outV = ''

for c in input_str:
    if any(c in x for x in vowels):
        outV += c
    elif c == " ":
        continue
    else:
        outC += c

print(outC)
print(outV)
