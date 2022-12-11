""" --- Day 10: Cathode-Ray Tube ---
--- Part Two ---
https://adventofcode.com/2022/day/10
"""
from enum import Enum

import day10_part1


def main():
    with open('input') as input_file:
        instructions = day10_part1.parse_input(input_file)

        clock = 0
        register_x = [1]

        for instruction in instructions:
            if instruction[0] == day10_part1.Instruction.NOOP:
                clock += 1
                register_x.append(register_x[clock - 1])
            elif instruction[0] == day10_part1.Instruction.ADD:
                clock += 1
                register_x.append(register_x[clock - 1])
                clock += 1
                register_x.append(register_x[clock - 1] + instruction[1])

        draw_screen(register_x)


def draw_screen(register):
    screen = [[]]

    for r in range(6):
        for c in range(40):
            clock = 40 * r + c
            sprite = [register[clock] - 1, register[clock], register[clock] + 1]

            print(clock, sprite)

            if c  in sprite:
                screen[r].append('#')
            else:
                screen[r].append(' ')
        screen.append([])

    s = ''
    for row in screen:
        for col in row:
            s += col
        s += '\n'
    print(s)



if __name__ == "__main__":
    main()
