""""--- Day 9: Rope Bridge ---
--- Part Two ---
https://adventofcode.com/2022/day/9
"""

import day9_part1


def main():
    with open('input') as input_moves:
        moves = day9_part1.parse_moves(input_moves)
        board = day9_part1.Board()
        rope = []
        for i in range(10):
            rope.append(day9_part1.Pointer(0, 0))

        for move in moves:
            for i in range(move.steps):
                rope[0].move(move.direction)
                for k in range(1, len(rope)):
                    rope[k].follow(rope[k - 1])
                board.visited(rope[9].x, rope[9].y)
        print(board.count_visited())


if __name__ == "__main__":
    main()
