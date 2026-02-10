#!/usr/bin/env python

import sys

count = len(sys.argv) - 1
if count:
    for i in range(1, count + 1):
        print(sys.argv[i].lower())
else:
    print("none")
