#!/usr/bin/env python

import sys

count = len(sys.argv) - 1
if count > 1:
    for i in range(count, 0, -1):
        print(sys.argv[i])
else:
    print("none")
