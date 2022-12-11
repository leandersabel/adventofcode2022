""""--- Day 9: Rope Bridge ---
--- Part One ---
https://adventofcode.com/2022/day/9
"""
import math
from enum import Enum


def main():
    with open('input') as input_moves:
        moves = parse_moves(input_moves)

        head = Pointer(0, 0)
        tail = Pointer(0, 0)
        board = Board()

        for move in moves:
            for i in range(move.steps):
                head.move(move.direction)
                tail.follow(head)
                board.visited(tail.x, tail.y)
        print(board.count_visited())


def parse_moves(input_moves):
    moves = []
    for move_string in input_moves:
        m = move_string.split()
        moves.append(Move(Direction(m[0]), int(m[1])))
    return moves


class Move:
    def __init__(self, direction, steps):
        self.direction = direction
        self.steps = int(steps)

    def __str__(self):
        return str(self.direction.name) + ': ' + str(self.steps)


class Direction(Enum):
    Up = 'U'
    Right = 'R'
    Down = 'D'
    Left = 'L'
    Up_Right = 'UR'
    Up_Left = 'UL'
    Down_Right = 'DR'
    Down_Left = 'DL'


class Pointer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == Direction.Up:
            self.y += 1
        elif direction == Direction.Right:
            self.x += 1
        elif direction == Direction.Down:
            self.y -= 1
        elif direction == Direction.Left:
            self.x -= 1
        elif direction == Direction.Up_Left:
            self.x -= 1
            self.y += 1
        elif direction == Direction.Up_Right:
            self.x += 1
            self.y += 1
        elif direction == Direction.Down_Left:
            self.x -= 1
            self.y -= 1
        elif direction == Direction.Down_Right:
            self.x += 1
            self.y -= 1

    def distance(self, other):
        return math.dist([self.x, self.y], [other.x, other.y])

    def follow(self, other):
        if self.distance(other) >= 2:
            if self.x == other.x:
                # Same column. Move up or down.
                if self.y < other.y:
                    self.move(Direction.Up)
                else:
                    self.move(Direction.Down)
            elif self.y == other.y:
                # Same row. Move left or right
                if self.x < other.x:
                    self.move(Direction.Right)
                else:
                    self.move(Direction.Left)
            else:
                # Neither same row nor same column
                if self.x < other.x and self.y < other.y:
                    self.move(Direction.Up_Right)
                elif self.x < other.x and self.y > other.y:
                    self.move(Direction.Down_Right)
                elif self.x > other.x and self.y < other.y:
                    self.move(Direction.Up_Left)
                elif self.x > other.x and self.y > other.y:
                    self.move(Direction.Down_Left)

    def __str__(self):
        return 'x:' + str(self.x) + ' y:' + str(self.y)


class Board:
    def __init__(self):
        self.board = {0: {0: 's'}}

    def visited(self, x, y):
        if y not in self.board:
            self.board[y] = dict()
        self.board[y][x] = '#'

    def count_visited(self):
        count = 0
        for row in self.board.values():
            for col in row.values():
                if col == '#':
                    count += 1
        return count


if __name__ == "__main__":
    main()
