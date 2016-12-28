#!/usr/bin/env python3

"""
Simple interactive Tic Tac Toe

a1 a2 a3
b1 b2 b3
c1 c2 c3

"""


def create_board():
    # Returns empty board as dict
    board = {}
    for letter in ['a', 'b', 'c']:
        for i in range(1, 4):
            board[letter + str(i)] = ' '
    return board


def label_board(board):
    # Over-writes existing board with cell labels
    for entry in board:
        board[entry] = entry


def print_board(**kwargs):
    # Print given board - this method accommodates differing cell widths
    s1 = '{a1}|{a2}|{a3}'.format(**kwargs)
    s2 = '{b1}|{b2}|{b3}'.format(**kwargs)
    s3 = '{c1}|{c2}|{c3}'.format(**kwargs)
    line = '-' * len(s1)
    print('\n{s1}\n{line}\n{s2}\n{line}\n{s3}\n'.format(s1=s1, s2=s2, s3=s3, line=line))


def create_scorekeeper():
    # Returns empty scorekeeper dictionary
    # For each of the eight winning row/column/diagonals:
    #     <count of X>, <count of O>, [<list of blank cells>]
    scorekeeper = {}
    for entry in ['a', 'b', 'c', '1', '2', '3', 'd1', 'd2']:
        scorekeeper[entry] = [0, 0, []]
    return scorekeeper


def update_scorekeeper(scorekeeper, board):
    # Add scores to scorekeeper dictionary

    # Score rows
    for letter in ['a', 'b', 'c']:
        scorekeeper[letter] = [0, 0, []]
        for number in [1, 2, 3]:
            key = letter + str(number)
            if board[key] == 'X':
                scorekeeper[letter][0] += 1
            elif board[key] == 'O':
                scorekeeper[letter][1] += 1
            else:
                scorekeeper[letter][2].append(key)

    # Score columns
    for number in [1, 2, 3]:
        scorekeeper[str(number)] = [0, 0, []]
        for letter in ['a', 'b', 'c']:
            key = letter + str(number)
            if board[key] == 'X':
                scorekeeper[str(number)][0] += 1
            elif board[key] == 'O':
                scorekeeper[str(number)][1] += 1
            else:
                scorekeeper[str(number)][2].append(key)

    # Score first diagonal
    for key in ['a1', 'b2', 'c3']:
        scorekeeper['d1'] = [0, 0, []]
        if board[key] == 'X':
            scorekeeper['d1'][0] += 1
        elif board[key] == 'O':
            scorekeeper['d1'][1] += 1
        else:
            scorekeeper['d1'][2].append(key)

    # Score second diagonal
    for key in ['a3', 'b2', 'c1']:
        scorekeeper['d2'] = [0, 0, []]
        if board[key] == 'X':
            scorekeeper['d2'][0] += 1
        elif board[key] == 'O':
            scorekeeper['d2'][1] += 1
        else:
            scorekeeper['d2'][2].append(key)
    print(scorekeeper)


def print_info():
    # Print instructions for humans
    print('''
This is a simple game of Tic Tac Toe.
Three marks in a horizontal, vertical, or diagonal row wins the game.
Human marks are 'X'. Machine marks are 'O'.
You have the following commands at your disposal:
\ta1 - c3: Mark that cell, if available
\ti: Print these instructions
\tp: Print labelled board
\tx: Exit
''')


def human_turn(active_board, example_board):
    while True:

        # print_info()

        response = input('a1-c3, i, p or x: ').strip().lower()

        print(response)

        if len(response) is 2 and response[0] in ['a', 'b', 'c'] and response[1] in ['1', '2', '3']:
            if active_board[response] == ' ':
                active_board[response] = "X"
                print_board(**active_board)
                return
            else:
                print('That cell is already taken')

        elif response == "i":
            print_info()

        elif response == "p":
            print_board(**example_board)

        elif response == "x":
            print("Exiting program")
            break

        else:
            print("try again")


def machine_turn(active_board):

    best_move_list = ['b2', 'a1', 'a3', 'c1', 'c3', 'b1', 'b3', 'a2', 'c2']

    for entry in best_move_list:
        if active_board[entry] == ' ':
            active_board[entry] = 'O'
            print_board(**active_board)
            return


def check_board(board, win_condition):
    # Returns list for win or threat conditions

    # Threat List will contain names of cells that should be blocked to prevent win
    threat_list = []

    # Row/col/dia score in form <count of X>, <count of O>, [<list of blank cells>]
    score_a = [0, 0, []]
    for entry in range(1, 4):
        if board['a' + str(entry)] == 'X':
            score_a[0] += 1
        elif board['a' + str(entry)] == 'O':
            score_a[1] += 1
        elif board['a' + str(entry)] == ' ':
            score_a[2].append('a' + str(entry))
    print(score_a)

    if score_a[0] == 3:
        win_condition = True
    elif score_a[0] == 2 and score_a[1] == 0:
        threat_list.append(score_a[2][0])

    print([win_condition, threat_list])

    return [win_condition, [threat_list]]


def main():

    win_condition = False

    # First, print board with labels in cells to identify them.
    example_board = create_board()
    label_board(example_board)
    print_board(**example_board)

    # Now, create the active board
    active_board = create_board()

    # Create scorekeeper object
    active_scorekeeper = create_scorekeeper()

    print_info()

    print_board(**active_board)

    while win_condition is False:

        human_turn(active_board, example_board)

        update_scorekeeper(active_scorekeeper, active_board)

        machine_turn(active_board)

        update_scorekeeper(active_scorekeeper, active_board)

if __name__ == "__main__":

    main()
