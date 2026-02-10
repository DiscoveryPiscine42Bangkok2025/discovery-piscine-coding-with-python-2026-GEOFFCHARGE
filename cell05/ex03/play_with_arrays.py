#!/usr/bin/env python

original =  [2, 8, 9, 48, 8, 22, -12, 2]
new = []
for i in original:
    if i > 5 and i + 2 not in new:
        new.append(i + 2)
print(f"Original array: {original}")
print(f"New array: {new}")
