#!/usr/bin/env python

import sys

if len(sys.argv) - 1 == 2:
    print([i for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1)])
else:
    print("none")
