#!/usr/bin/python3
"""
5-text_indentation module.

Defines a function that prints a text with 2 new lines after
each of these characters: '.', '?' and ':'.

There should be no leading or trailing spaces on any printed line.
"""


def text_indentation(text):
    """
    Print `text` with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    pending_space = False   # مسافة لسه ما طبعناها (نقرر لاحقاً نطبعها أو نلغيها)
    line_started = False    # هل بدأنا نطبع حروف في السطر الحالي؟

    for ch in text:
        if ch == ' ':
            # نأجل طباعة المسافة لين نعرف إذا بعدها علامة ترقيم أو حرف عادي
            pending_space = True
            continue

        if ch in ".?:":
            # علامة ترقيم:
            # لا نطبع المسافة المؤجلة قبلها (عشان ما يصير "Hola .")
            print(ch, end="")
            # نطبع سطرين جدد
            print("\n\n", end="")
            # نبدأ سطر جديد بعدها
            pending_space = False
            line_started = False
            continue

        # هنا حرف عادي (مو مسافة ومو علامة ترقيم)
        if line_started and pending_space:
            # في نص السطر: نطبع مسافة واحدة فقط
            print(" ", end="")
        # إذا السطر ما بدأ ولسه pending_space = True -> نتجاهلها (مسافات أول السطر)

        print(ch, end="")
        line_started = True
        pending_space = False

    # ما نطبع newline إضافي في النهاية
