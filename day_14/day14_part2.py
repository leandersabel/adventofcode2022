""" --- Day 14: Distress Signal ---
--- Part Two ---
https://adventofcode.com/2022/day/14
"""
import sys
from enum import Enum

import numpy as np

np.set_printoptions(threshold=sys.maxsize, linewidth=sys.maxsize, )


def main():
    with open('input') as f_in:
        paths = []
        max_dim = [-1, -1]
        for f_line in f_in:
            path = []
            f_points = f_line.strip().split('->')
            for f_pair in f_points:
                path.append([eval(i) for i in f_pair.split(',')])
                if path[-1][0] > max_dim[0]: max_dim[0] = path[-1][0]
                if path[-1][1] > max_dim[1]: max_dim[1] = path[-1][1]
            paths.append(path)

        # Add floor level
        max_dim[1] += 2
        max_dim[0] += 500
        cave = np.zeros([max_dim[1] + 1, max_dim[0] + 1])

        for path in paths:
            for i in range(len(path) - 1):
                p1 = path[i]
                p2 = path[i + 1]

                if p1[0] == p2[0]:  # x is the same
                    y_start = p1[1] if p1[1] <= p2[1] else p2[1]
                    y_end = p2[1] if p1[1] <= p2[1] else p1[1]
                    for s in range(y_start, y_end + 1):
                        cave[s][p1[0]] = 1
                elif p1[1] == p2[1]:  # y is the same
                    x_start = p1[0] if p1[0] <= p2[0] else p2[0]
                    x_end = p2[0] if p1[0] <= p2[0] else p1[0]
                    for s in range(x_start, x_end + 1):
                        cave[p1[1]][s] = 1
                else:
                    print('Error. Unexpected path from', p1, 'to', p2)

                #print_cave(cave)

        for i in range(len(cave[0] -1)):
            cave[len(cave)-1][i] = 1

        source_of_sand = [500, 0]
        status = STATUS.FALLING
        count = 0

        while status != STATUS.ABYSS and cave[source_of_sand[1]][source_of_sand[0]] == 0:
            sand = list(source_of_sand)
            status = STATUS.FALLING
            while status == STATUS.FALLING:
                status = drop_down(cave, sand)

            if status == STATUS.RESTING: count += 1
            if status == STATUS.ABYSS: print('Sand still falling off the board')

        print(cave[source_of_sand[1]][source_of_sand[0]])
        print_cave(cave)
        print('Rested', count)

        # 23858 too low




def drop_down(cave, sand):
    """A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or
    sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is
    blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving
    as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three
    possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next
    unit of sand is created back at the source. """

    # Check dimensions
    if sand[1] + 1 > len(cave) - 1 or sand[0] - 1 < 0 or sand[0] + 1 > len(cave[1]) - 1:
        return STATUS.ABYSS

    # Check directly below
    if cave[sand[1] + 1][sand[0]] == 0:
        sand[1] = sand[1] + 1
        return STATUS.FALLING

    # Directly below already blocked, check left
    elif cave[sand[1] + 1][sand[0] - 1] == 0:
        sand[1] = sand[1] + 1
        sand[0] = sand[0] - 1
        return STATUS.FALLING

    # Directly below already blocked & below left, check right
    elif cave[sand[1] + 1][sand[0] + 1] == 0:
        sand[1] = sand[1] + 1
        sand[0] = sand[0] + 1
        return STATUS.FALLING

        # Update the grid with the sand
    else:
        cave[sand[1]][sand[0]] = 2
        return STATUS.RESTING


def print_cave(cave):
    for row in cave:
        s = ''
        for node in row:
            if node == 0:
                s += '.'
            elif node == 1:
                s += '#'
            elif node == 2:
                s += 'o'
        print(s)


class STATUS(Enum):
    FALLING = 1
    RESTING = 2
    ABYSS = 3
    BLOCKED = 4


if __name__ == "__main__":
    main()
