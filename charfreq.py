#!/usr/bin/env python3

def character_frequency(filename):

    try:
        f = open(filename)
    except OSError:
        return None

    character = {}
    for line in f:
        for char in line:
            character[char] = character.get(char,0) +1
    f.close()
    return character
