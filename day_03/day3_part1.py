import numpy as np
import string


def get_priority(item):
    if item.islower():
        return string.ascii_lowercase.index(item) + 1
    elif item.isupper():
        return string.ascii_uppercase.index(item) + 27


with open('input') as rucksack_file:
    priorities = 0
    for rucksack in rucksack_file:
        # Remove newline character
        rucksack.strip()

        # Create two list of chars for each of the two compartments of the rucksack
        compartment1 = list(rucksack[slice(0, len(rucksack) // 2)])
        compartment2 = list(rucksack[slice(len(rucksack) // 2, len(rucksack))])

        # Intersect the two lists and re-format back into a string
        intersection = "".join((np.intersect1d(compartment1, compartment2)))

        priorities += get_priority(intersection)

    print("Total priorities: ", priorities)

