#!/usr/bin/env python

def greetings(text = "noble stranger"):
    if isinstance(text, str):
        print(f"Hello, {text}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
