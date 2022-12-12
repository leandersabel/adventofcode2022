""" --- Day 12: Hill Climbing Algorithm ---
--- Part One ---
https://adventofcode.com/2022/day/12
"""
import string
import sys

sys.setrecursionlimit(10000)


def main():
    with open('input') as input_map:
        hmap = parse_input(input_map)

        # This does not work
        """start = hmap[20][0]

        path = None
        max_depth = 0
        while path is None:
            max_depth += 1
            # print('Checking path for max depth', max_depth)
            path = test.find_path_to_end(0, max_depth)
            if path is None:
                print('No path of depth ', max_depth)
            else:
                print('Path found at depth ', max_depth)

            # 1521 too high
            # 1520 too high

        print(len(path))
        print(path)"""

        # Alternative approach, just brute-force it ...
        start = hmap[20][0]
        end = hmap[20][91]
        start.backtrack(0)

        # Print the map with a [ ] around the end field
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


def accessible(s1, s2):
    return string.ascii_lowercase.index(s2) <= string.ascii_lowercase.index(s1) + 1


class Node:
    def __init__(self, height, x, y):
        self.height = height
        self.x = x
        self.y = y
        self.path = None
        self.accessible_neighbours = []
        self.explored_at_max_depth = -1
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

    # This does not work
    """def find_path_to_end(self, current_depth, max_depth):

        if self.end:
            return [self]
        elif current_depth >= max_depth:
            return None
        elif self.explored_at_max_depth >= max_depth:
            return None
        else:
            # self.explored_at_max_depth = current_depth
            potential_paths = []
            for neighbour in self.accessible_neighbours:
                potential_path = neighbour.find_path_to_end(current_depth + 1, max_depth)
                if potential_path is not None:
                    potential_paths.append(potential_path)

            shortest_path_length = sys.maxsize
            shortest_potential_path = None
            for potential_path in potential_paths:
                if len(potential_path) < shortest_path_length:
                    print('Shorter path at', len(potential_path))
                    shortest_potential_path = potential_path

            if shortest_potential_path is not None:
                if self.path is None:
                    self.path = shortest_potential_path
                    self.path.append(self)
                    print('Update new')
                elif len(self.path) > len(shortest_potential_path) + 1:
                    self.path = shortest_potential_path
                    self.path.append(self)
                    print('Update better')
                else:
                    print('No update')
            return self.path"""


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
