#!/usr/bin/env python

def find_the_redheads(member):
    return [i for i, j in member.items() if j == "red"]
    
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
