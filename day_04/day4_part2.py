"""
--- Day 4: Camp Cleanup ---
--- Part One ---
https://adventofcode.com/2022/day/4
"""

import day4_part1


def main():
    with open('input') as assignments:
        partial_overlap = 0
        for assignment_pair in assignments:
            ranges = (day4_part1.process_assignment_pairs(assignment_pair.strip()))
            if determine_overlap(ranges):
                print("TRUE:  Ranges ", ranges, " overlap.")
                partial_overlap += 1
            else:
                print("FALSE: Ranges ", ranges, " do not overlap.")

        print('Assignments with partial overlap: ', partial_overlap)


def determine_overlap(ranges):
    """ Determine if one partially contained within the other.

    :rtype: bool
    :param ranges: Pair of ranges to be checked
    :type ranges: list[range]

    >>> determine_overlap([range(3, 7), range(4, 8)])
    True

    >>> determine_overlap(([range(6,6), range(4,6)]))
    True

    >>> determine_overlap([range(75, 76), range(18, 74)])
    False
    """

    assert len(ranges) == 2, f'Expecting 2 ranges, got {len(ranges)}'

    range1 = ranges[0]
    range2 = ranges[1]

    one_with_two = range2.start <= range1.start <= range2.stop or range2.start <= range1.stop <= range2.stop
    two_with_one = range1.start <= range2.start <= range1.stop or range1.start <= range2.stop <= range1.stop

    # one_with_two = range1.start <= range2.start or range1.stop <= range2.stop
    # two_with_one = range2.start <= range1.start or range2.stop <= range1.stop

    return one_with_two or two_with_one


if __name__ == "__main__":
    main()
