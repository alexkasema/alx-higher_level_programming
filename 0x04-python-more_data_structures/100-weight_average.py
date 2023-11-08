#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        i = 0
        j = 0
        for item in my_list:
            i += item[0] * item[1]
            j += item[1]
        return (i / j)
    return(0)
