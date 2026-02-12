#!/usr/bin/env python

import sys

if len(sys.argv) - 1 == 2:
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    if first < second:
        print([i for i in range(first, second + 1)])
    else:
        print([i for i in range(first, second - 1, -1)])
else:
    print("none")
