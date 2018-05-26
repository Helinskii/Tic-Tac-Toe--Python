import sys
import random

def display_board(board):
    board_layout = {'vertical':'|\n|\n|\n', 'horizontal':'-----------'}
    print(f"   |   |   \n {board[7]} | {board[8]} | {board[9]} \n   |   |   ")
    print("-" * 11)
    print(f"   |   |   \n {board[4]} | {board[5]} | {board[6]} \n   |   |   ")
    print("-" * 11)
    print(f"   |   |   \n {board[1]} | {board[2]} | {board[3]} \n   |   |   ")


def player_input(play, board):
    position = 0
    while position not in range(1, 10) or position in position_list:
        position = int(input("Choose your next position: (1-9)\n"))
        if position not in range(1, 10):
            print("Invalid Option. Choose a position from 1 - 9.\n")
        elif position in position_list:
            print("Position filled. Select a different position\n")

    position_list.append(position)
    if play % 2 == 0:
        place_marker(board, player_1, position)
    elif play % 2 == 1:
        place_marker(board, player_2, position)

def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)
    if win_check(board, marker):
        print("Congratulations! You've won the game.\n")
        sys.exit(0)

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

print('Welcome to Tic Tac Toe!')

player_1 = ''
while player_1 not in ('X', 'O'):
    player_1 = input('Player 1: Do you want to be X or O?\n').upper()
    if player_1 not in ('X', 'O'):
        print('Invalid Option')

if player_1 == 'X':
    player_2 = 'O'
else:
    player_2 = 'X'

if choose_first() == 'Player 1':
    print('Player 1 goes first.\n')
    play = 0
else:
    print('Player 2 goes first.\n')
    play = 1

answer = ''
while answer not in ('Yes', 'yes', 'No', 'no'):
    answer = input('Are you ready to play? Enter Yes or No.\n')
    if answer in ('Yes', 'yes'):
        break
    else:
        sys.exit(0)

position_list = []
board = [' '] * 10
while play in range(1, 10):
    player_input(play, board)
    play += 1
