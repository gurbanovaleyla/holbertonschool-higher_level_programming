#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = []
    for i in range(len(my_list)):
        if my_list[i] not in seen:
            seen.append(my_list[i])
    result = sum(seen)
    return result
