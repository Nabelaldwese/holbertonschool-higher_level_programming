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

    new_text = ""
    skip_space = True  # تخطي المسافات في بداية الأسطر

    for ch in text:
        if ch in ".?:":
            new_text += ch + "\n\n"
            skip_space = True  # ابدأ سطر جديد بدون مسافات
        else:
            if skip_space:
                if ch == " ":
                    continue
                skip_space = False
            new_text += ch

    print(new_text, end="")
