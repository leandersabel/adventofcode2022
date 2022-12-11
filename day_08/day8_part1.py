""""--- Day 8: Treetop Tree House ---
--- Part One ---
https://adventofcode.com/2022/day/8
"""

from enum import Enum


def main():
    with open('input') as input_lines:
        forest = Forest()
        for y, line in enumerate(input_lines):
            chars = list(line.strip())

            for x, char in enumerate(chars):
                forest.add_tree(x, y, int(char))

        forest.compute_visibility()
        print(forest.count_trees(True))


class Forest:

    def __init__(self):
        self.trees = list()

    def add_tree(self, x, y, height):
        # Check if a new row is needed
        if y >= len(self.trees):
            self.trees.append(list())

        self.trees[y].append(Tree(height, x, y))

    def compute_visibility(self):
        self.__compute_visibility(Direction.NORTH)
        self.__compute_visibility(Direction.EAST)
        self.__compute_visibility(Direction.SOUTH)
        self.__compute_visibility(Direction.WEST)

    def __compute_visibility(self, direction):
        if direction == Direction.NORTH:

            x = 0
            y = len(self.trees) - 1
            while x < len(self.trees[y]):
                max_height = -1
                while y >= 0:
                    self.trees[y][x].update_visibility(direction, self.trees[y][x].height > max_height)
                    max_height = max(max_height, self.trees[y][x].height)
                    y -= 1
                x += 1
                y = len(self.trees) - 1

        if direction == Direction.EAST:
            x = 0
            y = 0
            while y < len(self.trees):
                max_height = -1
                while x < len(self.trees[y]):
                    self.trees[y][x].update_visibility(direction, self.trees[y][x].height > max_height)
                    max_height = max(max_height, self.trees[y][x].height)
                    x += 1
                y += 1
                x = 0

        if direction == Direction.SOUTH:
            x = 0
            y = 0
            while x < len(self.trees[y]):
                max_height = -1
                while y < len(self.trees):
                    self.trees[y][x].update_visibility(direction, self.trees[y][x].height > max_height)
                    max_height = max(max_height, self.trees[y][x].height)
                    y += 1
                x += 1
                y = 0

        if direction == Direction.WEST:
            x = len(self.trees) - 1
            y = 0
            while y < len(self.trees):
                max_height = -1
                while x >= 0:
                    self.trees[y][x].update_visibility(direction, self.trees[y][x].height > max_height)
                    max_height = max(max_height, self.trees[y][x].height)
                    x -= 1
                y += 1
                x = len(self.trees) - 1

    def count_trees(self, visible):
        count = 0
        for row in self.trees:
            for tree in row:
                if tree.is_visible() == visible:
                    count += 1
        return count

    def look_around(self):
        for row in self.trees:
            for tree in row:
                self.__look_around(tree)

    def __look_around(self, tree):
        # look up
        x = tree.x
        y = tree.y - 1
        while y >= 0:
            other_tree = self.trees[y][x]
            if other_tree.height < tree.height:
                tree.add_visible_tree(other_tree, Direction.NORTH)
                y -= 1
            elif other_tree.height >= tree.height:
                tree.add_visible_tree(other_tree, Direction.NORTH)
                break

        # look right
        x = tree.x + 1
        y = tree.y
        while x < len(self.trees[y]):
            other_tree = self.trees[y][x]
            if other_tree.height < tree.height:
                tree.add_visible_tree(other_tree, Direction.EAST)
                x += 1
            elif other_tree.height >= tree.height:
                tree.add_visible_tree(other_tree, Direction.EAST)
                break

        # look down
        x = tree.x
        y = tree.y + 1
        while y < len(self.trees):
            other_tree = self.trees[y][x]
            if other_tree.height < tree.height:
                tree.add_visible_tree(other_tree, Direction.SOUTH)
                y += 1
            elif other_tree.height >= tree.height:
                tree.add_visible_tree(other_tree, Direction.SOUTH)
                break

        # look left
        x = tree.x - 1
        y = tree.y
        while x >= 0:
            other_tree = self.trees[y][x]
            if other_tree.height < tree.height:
                tree.add_visible_tree(other_tree, Direction.WEST)
                x -= 1
            elif other_tree.height >= tree.height:
                tree.add_visible_tree(other_tree, Direction.WEST)
                break

    def find_max_scenic_score(self):
        scores = []
        for row in self.trees:
            for tree in row:
                scores.append(tree.compute_scenic_score())
        scores.sort(reverse=True)
        return scores[0]

    def __str__(self):
        s = ""
        for row in self.trees:
            for tree in row:
                s += str(tree)
            s += '\n'
        return s


class Tree:

    def __init__(self, height, x, y):
        self.__visible = [None, None, None, None]
        self.height = height
        self.visible_trees = [list(), list(), list(), list()]
        self.x = x
        self.y = y

    def __str__(self):
        # return str(self.height) + '-' + str(self.__visible) + ' ' # debug for part 1
        return '[' + str(self.x) + ', ' + str(self.y) + '] ' + 'h:' + str(self.height) + ' s:' \
            + str(self.compute_scenic_score()) + ' '  # + str(self.visible_trees)  # debug for day 2

    def add_visible_tree(self, tree, direction):
        self.visible_trees[direction.value].append(tree)

    def is_visible(self):
        return self.__is_visible(Direction.NORTH) or self.__is_visible(Direction.EAST) or \
            self.__is_visible(Direction.SOUTH) or self.__is_visible(Direction.WEST)

    def __is_visible(self, direction) -> bool:
        """ Checks if a tree is visible from a given direction """
        return self.__visible[direction.value]

    def update_visibility(self, direction, visible):
        self.__visible[direction.value] = visible

    def compute_scenic_score(self):
        return len(self.visible_trees[0]) * len(self.visible_trees[1]) * \
            len(self.visible_trees[2]) * len(self.visible_trees[3])


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


if __name__ == "__main__":
    main()
