#!/usr/bin/python3

def uppercase(str):
    for c in str:
        chara = ord(c)
        if chara >= 97 and chara <= 122:
            chara -= 32
        print("{:c}".format(chara), end="")
    print()
