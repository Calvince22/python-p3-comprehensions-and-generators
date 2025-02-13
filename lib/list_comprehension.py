#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n%2 ==0]
    pass

def make_exclamation(sentence_list):
    return [item+'!' for item in sentence_list ]
    pass

print(make_exclamation(["hello","world"]))