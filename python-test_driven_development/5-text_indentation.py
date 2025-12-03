#!/usr/bin/python3
"""
Module for text_indentation function.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        if text[i] in ".?:":
            result += "\n\n"

            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1

    # اطبع كل سطر بدون مسافات زائدة بالبداية أو النهاية
    for line in result.split("\n"):
        print(line.strip())
