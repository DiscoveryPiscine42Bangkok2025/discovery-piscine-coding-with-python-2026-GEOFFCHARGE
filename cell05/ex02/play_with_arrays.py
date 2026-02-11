#!/usr/bin/env python

org = [2, 8, 9, 48, 8, 22, -12, 2]
new = [i + 2 for i in org if i > 5]
print(f"Original array: {org}")
print(f"New array: {new}")
