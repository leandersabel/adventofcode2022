def process_input(opp_coded, play_coded):
    if opp_coded == 'A':
        opp_clean = 'Rock'
    elif opp_coded == 'B':
        opp_clean = 'Paper'
    elif opp_coded == 'C':
        opp_clean = 'Scissors'
    if play_coded == 'X':
        play_clean = 'Rock'
    elif play_coded == 'Y':
        play_clean = 'Paper'
    elif play_coded == 'Z':
        play_clean = 'Scissors'
    return [opp_clean, play_clean]


def win_score(play, opp):
    # Draw
    if opp == play:
        print("Draw between ", opp, " and ", play)
        return 3

    # Winning conditions
    if (play == 'Rock' and opp == 'Scissors') or \
            (play == 'Scissors' and opp == 'Paper') or \
            (play == 'Paper' and opp == 'Rock'):
        print("Player wins with ", play, " against ", opp)
        return 6

    # Losing conditions
    else:
        print("Player loses with ", play, " against ", opp)
        return 0


def shape_score(play):
    if play == 'Rock':
        print('Player gets 1 point for Rock')
        return 1
    elif play == 'Paper':
        print('Player gets 2 points for Paper')
        return 2
    elif play == 'Scissors':
        print('Player gets 3 point for Scissors')
        return 3


with open('input') as strategy_guide:
    my_score = 0
    for line in strategy_guide:
        moves = process_input(line[0], line[2])
        opponent = moves[0]
        player = moves[1]
        my_score += win_score(player, opponent) + shape_score(player)
        print("Current score: ", my_score)
        print("\n")
    print('Total score: ', my_score)
