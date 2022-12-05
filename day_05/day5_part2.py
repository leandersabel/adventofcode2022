"""
--- Day 5: Supply Stacks ---
--- Part Two ---
https://adventofcode.com/2022/day/5
"""

import day5_part1


def main():

    with open('input_crates') as crates_from_file, open('input_moves') as moves_from_file:
        stacks = day5_part1.parse_crates(crates_from_file)
        moves = day5_part1.parse_moves(moves_from_file)

        for move in moves:
            n = int(move[0])
            # -1 because instructions use 1-based and stacks use 0-based indexing
            src = stacks[int(move[1]) - 1]
            trg = stacks[int(move[2]) - 1]

            # Create a new list from the n-th last elements of the source and extend the target
            trg.extend(src[-n:])
            # Remove the n-th last elements from the source
            del src[-n:]

        # Print out the top element of each stack
        for stack in stacks:
            print(stack[-1], end='')


if __name__ == "__main__":
    main()
