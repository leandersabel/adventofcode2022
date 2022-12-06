""""--- --- Day 6: Tuning Trouble ---
--- Part One ---
https://adventofcode.com/2022/day/5
"""


def main():
    with open('input') as input_streams:
        for input_stream in input_streams:
            for i in range(len(input_stream) - 3):
                # Create a dictionary from the keys, because it does not keep duplicate values
                dic = dict.fromkeys([input_stream[i], input_stream[i + 1], input_stream[i + 2], input_stream[i + 3]])

                # So if the length of the dictionary is still 4, they are all different
                if len(dic) == 4:
                    # +4 because the target value is the first index after the marker
                    print(i+4)
                    break


if __name__ == "__main__":
    main()
