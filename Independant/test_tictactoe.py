#!/usr/bin/env python3

"""
Testing for Simple interactive Tic Tac Toe
"""

import random

from tictactoe import clear_board


def test_clear_board():

    t = list(range(9))

    clear_board(t)

    assert t[random.randint(0, 8)] == ' '
