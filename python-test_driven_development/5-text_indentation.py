#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' and ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        if text[i] in ".?:":
            result = result.rstrip()
            print(result)
            print()
            result = ""
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1

    if result.strip() != "":
        print(result.strip(), end="")
