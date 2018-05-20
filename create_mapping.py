from __future__ import print_function
import sys
import string
import itertools
try:
    import cPickle as pickle
except:
    import pickle

from helper import classify, isword

i = 0
mapping = dict()
words = [line.rstrip('\n') for line in open(sys.argv[1], "r")]
for word in words:
    i += 1
    if i % 10000 == 0:
        # somehow print(str, flush=True) doesn't work in python2 even if
        # __future__.print_function is imported. This is a workaround
        print(".", end='')
        sys.stdout.flush()

    if not isword(word):
        # print(word)
        continue

    word = word.lower()
    category = classify(word)
    if category not in mapping:
        mapping[category] = list()
    mapping[category].append(word)

pickle.dump(mapping, open("words_mapping.p", 'wb'))
