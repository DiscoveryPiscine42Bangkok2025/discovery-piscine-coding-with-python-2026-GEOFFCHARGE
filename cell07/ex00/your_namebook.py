#!/usr/bin/env python

def array_of_names(person):
    return [i.capitalize() + " " + j.capitalize() for i, j in person.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
