"""
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/4
"""


def main():
    with open('input') as assignments:
        full_overlap = 0
        for assignment_pair in assignments:
            ranges = (process_assignment_pairs(assignment_pair.strip()))
            if determine_overlap(ranges):
                print("TRUE:  Ranges ", ranges, " overlap.")
                full_overlap += 1
            else:
                print("FALSE: Ranges ", ranges, " do not overlap.")

        print('Assignments with full overlap: ', full_overlap)


def process_assignment_pairs(assignment_pair):
    """ Convert a string of assignments into a list of ranges

    :rtype: list[range]
    :param assignment_pair: String of assignments from the input file
    :type assignment_pair: str

    >>> process_assignment_pairs("75-76,18-75")
    [range(75, 76), range(18, 75)]

    >>> process_assignment_pairs("2-54,1-50")
    [range(2, 54), range(1, 50)]
    """

    # Split the pair of assignments into list
    assignments = assignment_pair.split(',')

    # Input file should only contain pairs of 2 assignments
    assert len(assignments) == 2, f'Expecting 2 assignments. Got {len(assignments)}'

    assignment_list = []
    for assignment in assignments:
        assignment_list.append(assignment.split('-'))

    return [range(int(assignment_list[0][0]),
                  int(assignment_list[0][1])),
            range(int(assignment_list[1][0]),
                  int(assignment_list[1][1]))]


def determine_overlap(ranges):
    """ Determine if one fully contained within the other.

    :rtype: bool
    :param ranges: Pair of ranges to be checked
    :type ranges: list[range]

    >>> determine_overlap([range(3, 7), range(2, 8)])
    True

    >>> determine_overlap(([range(6,6), range(4,6)]))
    True

    >>> determine_overlap([range(75, 76), range(18, 75)])
    False
    """

    assert len(ranges) == 2, f'Expecting 2 ranges, got {len(ranges)}'

    range1 = ranges[0]
    range2 = ranges[1]

    one_in_two = range1.start >= range2.start and range1.stop <= range2.stop
    two_in_one = range2.start >= range1.start and range2.stop <= range1.stop

    return one_in_two or two_in_one


if __name__ == "__main__":
    main()
