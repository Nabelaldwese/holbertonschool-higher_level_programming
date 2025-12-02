#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Return a new list with all occurrences of search replaced by replace."""
    # ننسخ الليست الأصلية عشان ما نعدل عليها
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
