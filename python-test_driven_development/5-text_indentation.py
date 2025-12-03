#!/usr/bin/python3
"""
Module for text_indentation function.
Prints text with 2 new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' or ':' characters.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
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
            # Skip spaces after punctuation
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    # Print each line stripped of leading/trailing spaces
    for line in result.split("\n"):
        print(line.strip())
