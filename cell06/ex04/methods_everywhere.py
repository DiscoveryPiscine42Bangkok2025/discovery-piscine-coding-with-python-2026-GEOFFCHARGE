#!/usr/bin/env python

import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + "Z" * (8 - len(text)))

count = len(sys.argv) -1
if count:
    for i in range(1, count + 1):
        text = sys.argv[i]
        if len(text) > 8:
            shrink(text)
        else:
            enlarge(text)
else:
    print("none")
