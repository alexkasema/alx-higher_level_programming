#!/usr/bin/python3

""" A Text indentation function """


def text_indentation(text):
    """ prints text with 2 new lines after each of these characters: ., ? and :
    Args:
        text (str): Text to print.
    Raises:
        TypeError if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0

    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")

        if text[i] in ".?:" or text[i] == '\n':
            if text[i] in ".?:":
                print("\n")
            i += 1

            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1
