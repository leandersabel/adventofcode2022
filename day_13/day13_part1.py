""" --- Day 13: Distress Signal ---
--- Part One ---
https://adventofcode.com/2022/day/13
"""
import difflib
from enum import Enum


def main():
    with open('input') as input_lists:
        lines = (line.rstrip() for line in input_lists)
        lines = list(line for line in lines if line)  # Non-blank lines in a list

        pairs = []
        for i in range(0, len(lines), 2):
            pairs.append([eval(lines[i]), eval(lines[i + 1])])

        correct = 0
        for p, pair in enumerate(pairs):
            comp = compare(pair[0], pair[1])
            if comp == DIFF.SMALLER:
                correct += p + 1

        print('Correct order on: ', correct)


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
