#!/usr/bin/python3


def check_winner(board, symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True

    # Check diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][
            2] == symbol:
        return True

    if board[0][2] == symbol and board[1][1] == symbol and board[2][
            0] == symbol:
        return True

    return False


t = int(input())

for _ in range(t):
    board = [input() for _ in range(3)]

    if check_winner(board, 'X'):
        print('X')
    elif check_winner(board, 'O'):
        print('O')
    elif check_winner(board, '+'):
        print('+')
    else:
        print('DRAW')
