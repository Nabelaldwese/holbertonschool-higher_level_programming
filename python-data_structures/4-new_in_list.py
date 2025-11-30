#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # عمل نسخة من القائمة الأصلية
    new_list = my_list.copy()

    # فحص حدود الفهرس
    if idx < 0 or idx >= len(my_list):
        return new_list

    # تعديل النسخة فقط
    new_list[idx] = element
    return new_list
