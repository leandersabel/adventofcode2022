""" --- Day 17: Pyroclastic Flow ---
--- Part One ---
https://adventofcode.com/2022/day/17
"""
from enum import Enum


def main():
    """ In jet patterns, < means a push to the left, while > means a push to the right. The pattern above means that
    the jets will push a falling rock right, then right, then right, then left, then left, then right, and so on. If
    the end of the list is reached, it repeats. """
    jet_pattern = [Direction(direction) for direction in list(open("input").read())]

    """ The tall, vertical chamber is exactly seven units wide."""
    game_field = [[0 for c in range(7)] for r in range(3)]

    """Each rock appears so that its left edge is two units 
    away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, 
    if there isn't one). """

    rock_type = RockType.DASH
    rock = generate_rock(game_field, RockType.DASH)

    tick = 0
    rocks = 0
    max_rocks = 2022
    while rocks <= max_rocks:
        push_left_right(game_field, rock, jet_pattern, tick)

        if not drop_down(game_field, rock):
            rock_type = rock_type.next()
            rock = generate_rock(game_field, rock_type)
            rocks += 1

            #pretty_print(game_field, rock)

        tick += 1

    print('Height of the rock tower is', find_highest_rock(game_field), 'with', rocks, 'rocks')
    print(len(game_field))

    # Answer 3197

def drop_down(game_field, rock):

    falling = True
    for stone in rock:
        if stone[1] - 1 < 0 or game_field[stone[1] - 1][stone[0]] == 1:
            falling = False
    if falling:
        for stone in rock:
            stone[1] -= 1
    else:
        for stone in rock:
            game_field[stone[1]][stone[0]] = 1
    return falling


def push_left_right(game_field, rock, jet_pattern, tick):
    direction = jet_pattern[tick % len(jet_pattern)]
    #print('Pushing', direction)
    pushing = True

    for stone in rock:
        if stone[0] + direction.delta() < 0 or \
                stone[0] + direction.delta() >= 7 or \
                game_field[stone[1]][stone[0] + direction.delta()] == 1:
            pushing = False

    if pushing:
        for stone in rock:
            stone[0] += direction.delta()

    return pushing


def generate_rock(game_field, rock_type):
    update_game_field(game_field, rock_type)
    return [[2 + stone[0], len(game_field) - 1 - stone[1]] for stone in rock_type.value]


def update_game_field(game_field, rock_type):
    highest_rock = find_highest_rock(game_field)
    if len(game_field) - highest_rock < rock_type.height():
        game_field.extend([0 for c in range(7)] for r in range(highest_rock - len(game_field) + rock_type.height()))
    elif len(game_field) - highest_rock > rock_type.height():
        to_kill = len(game_field) - highest_rock - rock_type.height()
        del game_field[-to_kill]
        #print('Game field too high, killing', to_kill)

def find_highest_rock(game_field):
    for r, row in enumerate(game_field):
        if 1 not in row:
            return r
    return len(game_field)


def pretty_print(game_field, rock):
    for y, line in reversed(list(enumerate(game_field))):
        s = '|'
        for x, col in enumerate(line):
            if [x, y] in rock:
                s += '@'
            elif col == 1:
                s += '#'
            else:
                s += '.'
        s += '|'
        print(s)
    print('+———————+')


class Direction(Enum):
    LEFT = '<'
    RIGHT = '>'

    def delta(self):
        if self == Direction.LEFT:
            return -1
        elif self == Direction.RIGHT:
            return 1


class RockType(Enum):
    DASH = [[0, 0], [1, 0], [2, 0], [3, 0]]
    PLUS = [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]]
    J = [[2, 0], [2, 1], [2, 2], [1, 2], [0, 2]]
    I = [[0, 0], [0, 1], [0, 2], [0, 3]]
    O = [[0, 0], [0, 1], [1, 0], [1, 1]]

    def height(self):
        if self == RockType.DASH:
            return 4
        elif self == RockType.PLUS:
            return 6
        elif self == RockType.J:
            return 6
        elif self == RockType.I:
            return 7
        elif self == RockType.O:
            return 5

    def next(self):
        if self == RockType.DASH:
            return RockType.PLUS
        elif self == RockType.PLUS:
            return RockType.J
        elif self == RockType.J:
            return RockType.I
        elif self == RockType.I:
            return RockType.O
        elif self == RockType.O:
            return RockType.DASH


if __name__ == "__main__":
    main()
