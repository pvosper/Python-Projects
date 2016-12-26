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
            board[letter + str(i)] = '  '
    return board


def label_board(board):
    # Over-writes existing board with cell labels
    for entry in board:
        board[entry] = entry


def print_board(**kwargs):
    # Print given board
    print('\n{a1}|{a2}|{a3}'.format(**kwargs))
    print('-' * 8)
    print('{b1}|{b2}|{b3}'.format(**kwargs))
    print('-' * 8)
    print('{c1}|{c2}|{c3}\n'.format(**kwargs))


def print_info():
    # Print instructions for humans
    print('''
This is a simple game of Tic Tac Toe.
Three marks in a horizontal, vertical, or diagonal row wins the game.
Human moves are marked 'X'. Machine moves are 'O'.
You have the following commands at your disposal:
\ta1 - c3: Mark that cell, if available
\ti: Print these instructions
\tp: Print labelled board
\tx: Exit
''')


def human_turn():
    while True:

        # print_info()

        response = input('Enter move: ').strip().lower()

        print(response)

        if len(response) is 2 and response[0] in ['a', 'b', 'c'] and response[1] in ['1', '2', '3']:
            print('a1 - c3')

        elif response == "i":
            print_info()

        elif response == "p":
            print('print_board(example_board)')

        elif response == "x":
            print("Exiting program")
            break

        else:
            print("try again")


# active_board = {'a1': 'X', 'a2': 'O', 'a3': 'P'}
#
#
# def test(**kwargs):
#     print('{a1}|{a2}|{a3}'.format(**kwargs))
#     print('-' * 5)
#
# test(**active_board)


# def print_board():
#     print('{}|{}|{}'.format(ttt[0], ttt[1], ttt[2]))
#     print('-' * 5)
#     print('{}|{}|{}'.format(ttt[3], ttt[4], ttt[5]))
#     print('-' * 5)
#     print('{}|{}|{}\n'.format(ttt[6], ttt[7], ttt[8]))


# def clear_board(board):
#     for i in range(len(board)):
#         board[i] = ' '


# def human_turn():
#
#     print_board()
#
#     response = input('Enter move 0-8: ')
#
#     try:
#         response = int(response)
#         if response in range(len(ttt)):
#
#             if ttt[response] == ' ':
#                 ttt[response] = 'X'
#             else:
#                 print('invalid')
#         else:
#             print('try again')
#
#     except ValueError:
#
#         print('integer 0-8, please')
#
#
# def machine_turn():
#
#     bot_moves = [4, 1, 3, 5, 7, 0, 2, 6, 8]
#
#     for i in range(len(bot_moves)):
#         if ttt[i] == ' ':
#             ttt[i] = 'O'
#             return
#
#
# def test_three_across(cell_a, cell_b, cell_c):
#     if cell_a == cell_b and cell_b == cell_c:
#         print('Win!')


def main():

    # First, print board with labels in cells to identify them.
    example_board = create_board()
    label_board(example_board)
    print_board(**example_board)

    # Now, create the active board
    active_board = create_board()
    print_board(**active_board)

    print_info()

    human_turn()

#        machine_turn()


if __name__ == "__main__":

    main()
