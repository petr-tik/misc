#! /usr/bin/env python3

""" Given random 9 letters (possibly with repititions) and a dictionary
return the longest possible word """


with open('/usr/share/dict/words') as f:
    dictionary = [x.lower() for x in f.read.splitlines()]
