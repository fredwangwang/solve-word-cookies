#!/usr/bin/python3

import sys
import string
import itertools
import pickle

from helper import classify


if len(sys.argv) == 1:
    print("Usage: python " + sys.argv[0] + " letters num")
    print("E.g:   python " + sys.argv[0] + " apelp 4")
    exit(0)

mapping = pickle.load(open("words_mapping.p", "rb"))

combinations = map(''.join, list(
    itertools.combinations(sys.argv[1], int(sys.argv[2]))))

answer = set()
for combo in combinations:
    category = classify(combo)
    if category in mapping:
        for word in mapping[category]:
            answer.add(word)
print(sorted(list(answer)))
