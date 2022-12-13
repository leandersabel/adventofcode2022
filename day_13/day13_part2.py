""" --- Day 13: Distress Signal ---
--- Part Two ---
https://adventofcode.com/2022/day/13
"""
import difflib
from enum import Enum


def main():
    with open('input') as input_lists:
        lines = (line.rstrip() for line in input_lists)
        lines = list(line for line in lines if line)  # Non-blank lines in a list

        unsorted_lists = []
        for lst in lines:
            unsorted_lists.append(eval(lst))

        sorted_lists = []
        marker_1 = [2]
        marker_2 = [6]

        sorted_lists.append(marker_1)
        sorted_lists.append(marker_2)

        while len(unsorted_lists) > 0:
            unsorted_list = unsorted_lists.pop()

            i = 0
            while i < len(sorted_lists) and unsorted_list is not None:
                dif_i = compare(unsorted_list, sorted_lists[i])
                if dif_i == DIFF.SMALLER:
                    sorted_lists.insert(i, unsorted_list)
                    unsorted_list = None
                i += 1
            if unsorted_list is not None:
                sorted_lists.append(unsorted_list)

        print(sorted_lists)
        i1 = sorted_lists.index(marker_1) + 1
        i2 = sorted_lists.index(marker_2) + 1

        print('decoder key: ', i1 * i2)


def compare(left, right):
    """ If both values are integers, the lower integer should come first. If the left integer is lower than the right
    integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are
    not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input."""
    if type(left) == int and type(right) == int:
        if left == right:
            return DIFF.SAME
        else:
            return DIFF(left < right)

    """If both values are lists, compare the first value of each list, then the second value, and so on. If the left 
    list runs out of items first, the inputs are in the right order. If the right list runs out of items first, 
    the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about 
    the order, continue checking the next part of the input."""
    if type(left) == list and type(right) == list:
        for l_i, r_i in zip(left, right):
            comp = compare(l_i, r_i)
            if comp != DIFF.SAME:
                return comp
        return compare(len(left), len(right))

    """If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, 
    then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list 
    containing 2); the result is then found by instead comparing [0,0,0] and [2]. """
    if type(left) == int:
        return compare([left], right)
    else:
        return compare(left, [right])


class DIFF(Enum):
    SMALLER = True
    LARGER = False
    SAME = None


if __name__ == "__main__":
    main()
