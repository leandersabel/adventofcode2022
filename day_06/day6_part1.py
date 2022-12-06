""""--- --- Day 6: Tuning Trouble ---
--- Part One ---
https://adventofcode.com/2022/day/5
"""


def main():
    with open('input') as input_streams:
        for input_stream in input_streams:
            for i in range(len(input_stream) - 3):
                # Create a set from the keys, because it does not keep duplicate values
                s = {input_stream[i], input_stream[i + 1], input_stream[i + 2], input_stream[i + 3]}

                # So if the length of the set is still 4, they are all different
                if len(s) == 4:
                    # +4 because the target value is the first index after the marker
                    print(i+4)
                    break


if __name__ == "__main__":
    main()
