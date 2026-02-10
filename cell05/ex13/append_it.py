#!/usr/bin/env python

import sys

count = len(sys.argv) - 1
if count:
    for i in range(1, count + 1):
        if not sys.argv[i].endswith("ism"):
            print(sys.argv[i] + "ism")
else:
    print("none")
