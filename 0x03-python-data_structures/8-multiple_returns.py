#!/usr/bin/python3

def multiple_returns(sentence):
    s_len = len(sentence)

    if s_len == 0:
        c = None
    else:
        c = sentence[:1]
    return ((s_len, c))
