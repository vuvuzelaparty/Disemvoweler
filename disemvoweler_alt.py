#!/usr/bin/env python

# this is a slightly edited response from another post in the reddit link
# https://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/cfng0od
# i added this because it's cool

import sys

if len(sys.argv) != 2:
    print 'Usage:'
    print '    ./disemvoweler "<input string>"'
    print 'Example:'
    print '    ./disemvoweler "two drums and a cymbal fall off a cliff"'
    sys.exit()

text = sys.argv[1]
vowels = 'aeiou'
print(''.join(letter for letter in text if letter not in vowels)).replace(' ', '')
print(''.join(letter for letter in text if letter in vowels))
