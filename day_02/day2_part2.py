# Rock defeats Scissors,
# Scissors defeats Paper, and
# Paper defeats Rock.

def process_input(opp_coded, outcome_coded):
    if opp_coded == 'A':
        opp_clean = 'Rock'
    elif opp_coded == 'B':
        opp_clean = 'Paper'
    elif opp_coded == 'C':
        opp_clean = 'Scissors'
    if outcome_coded == 'X':
        outcome_clean = 'lose'
    elif outcome_coded == 'Y':
        outcome_clean = 'draw'
    elif outcome_coded == 'Z':
        outcome_clean = 'win'
    return [opp_clean, outcome_clean]


def decide_move(opp, out):
    if out == 'draw':
        return opp
    elif out == 'win':
        if opp == 'Scissors':
            return 'Rock'
        elif opp == 'Paper':
            return 'Scissors'
        elif opp == 'Rock':
            return 'Paper'
    elif out == 'lose':
        if opp == 'Scissors':
            return 'Paper'
        elif opp == 'Paper':
            return 'Rock'
        elif opp == 'Rock':
            return 'Scissors'


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
        strategy = process_input(line[0], line[2])
        opponent = strategy[0]
        player = decide_move(opponent, strategy[1])
        print("Player trying to ", strategy[1], " so playing ", player, " against ", opponent)
        my_score += win_score(player, opponent) + shape_score(player)
        print("Current score: ", my_score)
        print("\n")
    print('Total score: ', my_score)
