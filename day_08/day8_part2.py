""""--- Day 8: Treetop Tree House ---
--- Part Two ---
https://adventofcode.com/2022/day/5
"""

import day8_part1


def main():
    with open('input') as input_lines:
        forest = day8_part1.Forest()
        for y, line in enumerate(input_lines):
            chars = list(line.strip())

            for x, char in enumerate(chars):
                forest.add_tree(x, y, int(char))

        # forest.compute_visibility()
        forest.look_around()
        print('Most scenic view:', forest.find_max_scenic_score())


if __name__ == "__main__":
    main()
