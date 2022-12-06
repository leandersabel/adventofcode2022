""""--- --- Day 6: Tuning Trouble ---
--- Part Two ---
https://adventofcode.com/2022/day/5
"""


def main():
    with open('input') as input_streams:
        for input_stream in input_streams:
            for i in range(len(input_stream) - 13):
                # Create a dictionary from the keys, because it does not keep duplicate values
                s = []
                for j in range(14):
                    s.append(input_stream[i+j])

                dic = dict.fromkeys(s)
                #print(len(dic))

                # So if the length of the dictionary is still 4, they are all different
                if len(dic) == 14:
                    # +14 because the target value is the first index after the marker
                    print(i+14)
                    break


if __name__ == "__main__":
    main()
