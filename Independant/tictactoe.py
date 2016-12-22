#!/usr/bin/env python3

'''
Simple interactive Tic Tac Toe
'''

ttt = list(range(9))

def print_board():
    print('{}|{}|{}'.format(ttt[0], ttt[1], ttt[2]))
    print('-' * 5)
    print('{}|{}|{}'.format(ttt[3], ttt[4], ttt[5]))
    print('-' * 5)
    print('{}|{}|{}\n'.format(ttt[6], ttt[7], ttt[8]))


def clear_board():
    for i in range(len(ttt)):
        ttt[i] = ' '


def human_turn():
    response = input()

    if response in range(len(ttt)):

        if ttt[response] == ' ':
            ttt[response] = 'X'

        print_board()


def main():
    # First, print board with numbers in cells to identify them. Then clear ttt list and reprint blank board.
    print_board()
    clear_board()
    print_board()

    while True:
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

            print_board()

        except ValueError:

            print('integer 0-8, please')


main()