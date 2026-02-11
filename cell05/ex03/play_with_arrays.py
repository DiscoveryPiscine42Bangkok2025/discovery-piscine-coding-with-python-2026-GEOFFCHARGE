#!/usr/bin/env python

org = [2, 8, 9, 48, 8, 22, -12, 2]
new = []
for i in org:
    if i > 5 and i + 2 not in new:
        new.append(i + 2)
print(f"Original array: {org}")
print(f"New array: {new}")
