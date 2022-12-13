""" --- Day 12: Hill Climbing Algorithm ---
--- Part One ---
https://adventofcode.com/2022/day/12
"""
import string
import sys

sys.setrecursionlimit(2000)


def main():
    with open('input') as input_map:
        hmap = parse_input(input_map)

        start = hmap[20][0]
        end = hmap[20][91]
        start.backtrack(0)

        print_map(hmap)

        print('Target field is ', end.depth, 'moves away')


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
        s = ""
        for col in row:
            if col.depth != sys.maxsize:
                if col.end:
                    s += '['
                s += ' ' + str(col.depth) + ' '
                if col.end:
                    s += ']'
            else:
                s += ' ' + str(col.height) + ' '
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


def accessible(s1, s2):
    return string.ascii_lowercase.index(s2) <= string.ascii_lowercase.index(s1) + 1


class Node:
    def __init__(self, height, x, y):
        self.height = height
        self.x = x
        self.y = y
        self.accessible_neighbours = []
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
        for neighbour in self.accessible_neighbours:
            neighbour.backtrack(depth+1)

    def update_neighbours(self, hmap):
        # Check left
        if self.x > 0 and accessible(self.height, hmap[self.y][self.x - 1].height):
            self.accessible_neighbours.append(hmap[self.y][self.x - 1])

        # Check right
        if self.x + 1 < len(hmap[self.y]) and accessible(self.height, hmap[self.y][self.x + 1].height):
            self.accessible_neighbours.append(hmap[self.y][self.x + 1])

        # Check up
        if self.y > 0 and accessible(self.height, hmap[self.y - 1][self.x].height):
            self.accessible_neighbours.append(hmap[self.y - 1][self.x])

        # Check down
        if self.y + 1 < len(hmap) and accessible(self.height, hmap[self.y + 1][self.x].height):
            self.accessible_neighbours.append(hmap[self.y + 1][self.x])

    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ':' + self.height + ' n:' + \
            str(len(self.accessible_neighbours)) + ' End: ' + str(self.end) + ']'


if __name__ == "__main__":
    main()
