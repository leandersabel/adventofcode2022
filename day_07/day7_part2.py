""""--- Day 7: No Space Left On Device ---
--- Part Two ---
https://adventofcode.com/2022/day/7
"""

import day7_part1


def main():
    # Values from puzzle input
    total_file_system = 70000000
    required_space = 30000000

    with open('input') as terminal_log:
        directories = day7_part1.parse_input(terminal_log)

        root_dir_size = directories.get_size()
        space_to_clear = - (total_file_system - root_dir_size - required_space)
        print('Space to clear:', space_to_clear)

        candidates = directories.get_directories_above(space_to_clear)

        print('Sorted')
        candidates.sort(reverse=True)
        for c in candidates:
            print('Folder', c.name, 'size:', c.get_size())


if __name__ == "__main__":
    main()
