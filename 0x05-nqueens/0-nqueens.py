#!/usr/bin/python3
""" Solves N Queen Problem """

import sys


def safety_check(Board, line, i):
    """ Checking if can insert Quen at column
    i in that line on Board """
    for n in range(line):
        if (Board[n] == i or
                Board[n] + line - n == i or
                Board[n] + n - line == i):
            return False
    return True


def line_fill(Board, line):
    """ Filling eaxh line of the board with
    correct index """
    for i in range(len(Board)):
        if safety_check(Board, line, i):
            Board[line] = i
            if line < len(Board) - 1:
                line_fill(Board, line + 1)
            else:
                print([[i, Board[i]] for i in range(len(Board))])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

Board = [-1 for i in range(n)]
line_fill(Board, 0)
