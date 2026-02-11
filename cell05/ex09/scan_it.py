#!/usr/bin/env python

import sys

if len(sys.argv) - 1 == 2 and sys.argv[2].count(sys.argv[1]):
    print(sys.argv[2].count(sys.argv[1]))
else:
    print("none")
