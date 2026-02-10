#!/usr/bin/env python

import sys

if len(sys.argv) - 1 == 1 and sys.argv[1].count("z"):
    print("z" * sys.argv[1].count("z"))
else:
    print("none")
