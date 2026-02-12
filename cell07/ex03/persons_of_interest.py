#!/usr/bin/env python

def sort_date_of_birth(item):
    return item[1]["date_of_birth"]

def famous_births(women):
    for _, j in sorted(women.items(), key=sort_date_of_birth):
        print(f"{j["name"]} is a great scientist born in {j["date_of_birth"]}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
