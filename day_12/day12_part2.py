""" --- Day 12: Hill Climbing Algorithm ---
--- Part Two ---
https://adventofcode.com/2022/day/12
"""
import string
import sys
import day12_part1

sys.setrecursionlimit(2000)


def main():
    with open('input') as input_map:
        hmap = parse_input(input_map)

        # Alternative approach, just brute-force it ...
        start = hmap[20][0]
        end = hmap[20][91]
        end.backtrack(0)

        day12_part1.print_map(hmap)

        # Now find the closest a
        min_dist_a = sys.maxsize
        for row in hmap:
            for col in row:
                if col.height == 'a':
                    if col.depth < min_dist_a:
                        min_dist_a = col.depth

        print('Minimum distance form an a is', min_dist_a)


def parse_input(input_map):
    hmap = []
    for ry, map_input_row in enumerate(input_map):
        cols = list(map_input_row.strip())
        nodes = []
        for cx, col in enumerate(cols):
            nodes.append(Node(col, cx, ry))
        hmap.append(nodes)

    for row in hmap:
        for node in row:
            node.update_neighbours(hmap)

    return hmap


def print_map(hmap):
    for row in hmap:
        s = ''
        for col in row:
            s += str(col)
        print(s)


def update_start_end(height_map):
    start = None
    end = None
    for r, row in enumerate(height_map):
        for c, col in enumerate(row):
            if col == 'S':
                start = [r, c]
                height_map[r][c] = 'a'
            elif col == 'E':
                end = [r, c]
                height_map[r][c] = 'z'
    return [start, end]


def accessible_from(source, destination):
    return string.ascii_lowercase.index(destination) <= string.ascii_lowercase.index(source) + 1


class Node:
    def __init__(self, height, x, y):
        self.height = height
        self.x = x
        self.y = y
        self.accessible_to_neighbours = []
        self.depth = sys.maxsize

        if self.height == 'S':
            self.height = 'a'
            self.start = True
        else:
            self.start = False

        if self.height == 'E':
            self.height = 'z'
            self.end = True
            self.path = [self]
        else:
            self.end = False

    def backtrack(self, depth):
        if self.depth > depth:
            self.depth = depth
        elif self.depth <= depth:
            return
        for neighbour in self.accessible_to_neighbours:
            neighbour.backtrack(depth + 1)

    def update_neighbours(self, hmap):
        # Check left
        if self.x > 0 and accessible_from(hmap[self.y][self.x - 1].height, self.height):
            self.accessible_to_neighbours.append(hmap[self.y][self.x - 1])

        # Check right
        if self.x + 1 < len(hmap[self.y]) and accessible_from(hmap[self.y][self.x + 1].height, self.height):
            self.accessible_to_neighbours.append(hmap[self.y][self.x + 1])

        # Check up
        if self.y > 0 and accessible_from(hmap[self.y - 1][self.x].height, self.height):
            self.accessible_to_neighbours.append(hmap[self.y - 1][self.x])

        # Check down
        if self.y + 1 < len(hmap) and accessible_from(hmap[self.y + 1][self.x].height, self.height):
            self.accessible_to_neighbours.append(hmap[self.y + 1][self.x])

    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ':' + self.height + ' n:' + \
            str(len(self.accessible_to_neighbours)) + ' End: ' + str(self.end) + ']'


if __name__ == "__main__":
    main()
