"""
--- Day 5: Supply Stacks ---
--- Part One ---
https://adventofcode.com/2022/day/5
"""


def main():
    with open('input_crates') as crates_from_file, open('input_moves') as moves_from_file:
        stacks = parse_crates(crates_from_file)
        moves = parse_moves(moves_from_file)

        for move in moves:
            for i in range(int(move[0])):
                # -1 because instructions use 1-based and stacks use 0-based indexing
                # src = stacks[int(move[1])-1], trg = stacks[int(move[2]) - 1]
                stacks[int(move[2]) - 1].append(stacks[int(move[1]) - 1].pop())

        # Print out the top element of each stack
        for stack in stacks:
            print(stack[-1], end='')


def parse_crates(crates_from_file):
    """ Read crates from file organize them in a list of stacks for easy access

    :param crates_from_file:
    """

    # Read each row of crates into a new list
    rows = list()
    for row_from_file in crates_from_file:
        rows.append(row_to_list(row_from_file))

    # Reverse order to start with the crates at the bottom
    rows.reverse()

    # Transpose for easy access of each stack
    return transpose(rows)


def transpose(rows):
    """ Transpose the list of lists, i.e. move each 'column' from the input matrix into a row

    >>> transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    >>> transpose([[1, 2, 3], [4, 5, 6], [7, 8]])
    [[1, 4, 7], [2, 5, 8], [3, 6]]

    """
    # Create a list of list to hold the stacks, based on the number of crates in the bottom layer of the pile
    stacks = list()
    for r in range(len(rows[0])):
        stacks.append(list())

    # Transpose the list of lists
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] != " ":
                stacks[c].append(rows[r][c])

    return stacks


def row_to_list(row_from_file: str) -> list:
    """ Convert the representation of a row of crates to a list

    >>> row_to_list('    [H]         [H]         [V]')
    [' ', 'H', ' ', ' ', 'H', ' ', ' ', 'V']

    >>> row_to_list('[P] [B] [B] [P] [Q] [S] [L] [H] [B]')
    ['P', 'B', 'B', 'P', 'Q', 'S', 'L', 'H', 'B']
    """

    row_from_file = list(row_from_file)
    row = list()
    for i in range(1, len(row_from_file), 4):
        row.append(row_from_file[i])
    return row


def parse_moves(moves_from_file):
    """ Parse the moves input file into a list of lists with instructions

    :param moves_from_file:
    """
    moves = list()
    for move_string in moves_from_file:
        move = move_string.split()
        # Remove unnecessary elements
        move.remove('move')
        move.remove('from')
        move.remove('to')
        moves.append(move)

    return moves


if __name__ == "__main__":
    main()
