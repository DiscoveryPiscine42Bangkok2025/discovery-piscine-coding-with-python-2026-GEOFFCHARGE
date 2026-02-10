#!/usr/bin/env python

import sys

count = len(sys.argv) - 1
if count:
    print(f"parameters: {count}")
    for i in range(1, count + 1):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
else:
    print("none")
