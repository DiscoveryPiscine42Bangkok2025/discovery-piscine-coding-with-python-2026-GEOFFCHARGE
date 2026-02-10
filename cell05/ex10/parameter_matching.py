#!/usr/bin/env python

import sys

if len(sys.argv) -1 == 1:
    if sys.argv[1] == input("What was the parameter? "):
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
