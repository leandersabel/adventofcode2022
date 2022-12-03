import numpy as np
import string


def get_priority(item):
    if item.islower():
        return string.ascii_lowercase.index(item) + 1
    elif item.isupper():
        return string.ascii_uppercase.index(item) + 27


with open('input') as rucksack_file:
    lines = rucksack_file.readlines()
    priorities = 0

    for i in range(0, len(lines), 3):
        backpack1 = list(lines[i].strip())
        backpack2 = list(lines[i+1].strip())
        backpack3 = list(lines[(i+2)].strip())
        intersection = "".join((np.intersect1d(np.intersect1d(backpack1, backpack2), backpack3)))
        priorities += get_priority(intersection)

    print("Total priorities: ", priorities)
