#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)

    roman_numbers = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    roman = list(roman_string.upper())

    res = 0
    temp = 0

    for letter in roman:
        if letter in roman_numbers:
            res += roman_numbers[letter]
            if roman_numbers[letter] > temp:
                res -= temp * 2
            temp = roman_numbers[letter]
        else:
            return (0)
    return (res)
