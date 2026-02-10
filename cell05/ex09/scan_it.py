#!/usr/bin/env python

import sys, re

if len(sys.argv) - 1 == 2:
    print(len(re.findall(sys.argv[1], sys.argv[2])))
else:
    print("none")
