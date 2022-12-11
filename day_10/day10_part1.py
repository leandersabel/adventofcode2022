""" --- Day 10: Cathode-Ray Tube ---
--- Part One ---
https://adventofcode.com/2022/day/10
"""
from enum import Enum


def main():
    with open('input') as input_file:
        instructions = parse_input(input_file)

        clock = 0
        register_x = [1]

        for instruction in instructions:
            if instruction[0] == Instruction.NOOP:
                clock += 1
                register_x.append(register_x[clock - 1])
            elif instruction[0] == Instruction.ADD:
                clock += 1
                register_x.append(register_x[clock - 1])
                clock += 1
                register_x.append(register_x[clock - 1] + instruction[1])

        signal_strength = register_x[20 - 1] * 20 + register_x[60 - 1] * 60 + register_x[100 - 1] * 100 + \
            register_x[140 - 1] * 140 + register_x[180 - 1] * 180 + register_x[220 - 1] * 220

        print(signal_strength)


def parse_input(input_file):
    instructions = []
    for input_line in input_file:
        split_line = input_line.split()
        instruction = [Instruction(split_line[0])]
        if instruction[0] == Instruction.ADD:
            instruction.append(int(split_line[1]))
        instructions.append(instruction)
    return instructions


class Instruction(Enum):
    NOOP = 'noop'
    ADD = 'addx'


if __name__ == "__main__":
    main()
