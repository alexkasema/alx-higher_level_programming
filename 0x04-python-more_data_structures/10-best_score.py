#!/usr/bin/python3

def best_score(a_dictionary):
    name = None
    score = 0
    if type(a_dictionary) is dict:
        for k, v in a_dictionary.items():
            if v > score:
                score = v
                name = k
    return (name)
