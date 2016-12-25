#!/usr/bin/env python3

"""
Simple interactive Tic Tac Toe

a1 a2 a3
b1 b2 b3
c1 c2 c3

"""

# board should be dict

ttt = list(range(9))

# dict start with end with

def create_board():
    # Returns empty board as dict
    board = {}
    for letter in ['a', 'b', 'c']:
        for i in range(1,4):
            board[letter + str(i)] = ' '
    return board

def label_board(board):
    # Over-writes existing board with cell labels
    for entry in board:
        board[entry] = entry


active_board = {'a1': 'X', 'a2': 'O', 'a3': 'P'}


def test(**kwargs):
    print('{a1}|{a2}|{a3}'.format(**kwargs))
    print('-' * 5)

test(**active_board)


def print_board():
    print('{}|{}|{}'.format(ttt[0], ttt[1], ttt[2]))
    print('-' * 5)
    print('{}|{}|{}'.format(ttt[3], ttt[4], ttt[5]))
    print('-' * 5)
    print('{}|{}|{}\n'.format(ttt[6], ttt[7], ttt[8]))


def clear_board(board):
    for i in range(len(board)):
        board[i] = ' '


def human_turn():

    print_board()

    response = input('Enter move 0-8: ')

    try:
        response = int(response)
        if response in range(len(ttt)):

            if ttt[response] == ' ':
                ttt[response] = 'X'
            else:
                print('invalid')
        else:
            print('try again')

    except ValueError:

        print('integer 0-8, please')


def machine_turn():

    bot_moves = [4, 1, 3, 5, 7, 0, 2, 6, 8]

    for i in range(len(bot_moves)):
        if ttt[i] == ' ':
            ttt[i] = 'O'
            return


def test_three_across(cell_a, cell_b, cell_c):
    if cell_a == cell_b and cell_b == cell_c:
        print('Win!')



def main():

    # First, print board with numbers in cells to identify them. Then clear ttt list and reprint blank board.
    print_board()
    clear_board(ttt)

    while True:

        human_turn()

        machine_turn()


if __name__ == "__main__":

    main()