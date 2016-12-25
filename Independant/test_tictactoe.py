#!/usr/bin/env python3

"""
Testing for Simple interactive Tic Tac Toe
"""


from tictactoe import create_board, label_board


def test_create_board():

    c = create_board()

    assert len(c) == 9
    assert c['a1'] == ' '
    assert c['b2'] == ' '
    assert c['c3'] == ' '


def test_label_board():

    c = create_board()

    label_board(c)

    assert len(c) == 9
    assert c['a1'] == 'a1'
    assert c['b2'] == 'b2'
    assert c['c3'] == 'c3'
