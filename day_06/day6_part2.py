""""--- --- Day 6: Tuning Trouble ---
--- Part Two ---
https://adventofcode.com/2022/day/5
"""


def main():
    with open('input') as input_streams:
        for input_stream in input_streams:
            for i in range(len(input_stream) - 13):
                # Create a set from the keys, because it does not keep duplicate values
                s = set()
                for j in range(14):
                    s.add(input_stream[i+j])

                # So if the length of the set is still 14, they are all different
                if len(s) == 14:
                    # +14 because the target value is the first index after the marker
                    print(i+14)
                    break


if __name__ == "__main__":
    main()
