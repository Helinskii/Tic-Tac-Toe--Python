import sys

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
    if play % 2 == 1:
        place_marker(board, 'X', position)
        print(board) # delete
        print(position_list) # delete
    else:
        place_marker(board, 'O', position)
        print(board) # delete
        print(position_list) # delete

def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)


print('Welcome to Tic Tac Toe!')

player_1 = ''
while player_1 not in ('X', 'x', 'O', 'o'):
    player_1 = input('Do you want to be X or O?\n')
    if player_1 not in ('X', 'x', 'O', 'o'):
        print('Invalid Option')

if player_1 in ('X', 'x'):
    player_1 = 'X'
    player_2 = 'O'
    print('Player 1 will go first.\n')
else:
    player_1 = 'O'
    player_2 = 'X'
    print('Player 2 will go first.\n')

answer = ''
while answer not in ('Yes', 'yes', 'No', 'no'):
    answer = input('Are you ready to play? Enter Yes or No.\n')
    if answer in ('Yes', 'yes'):
        break
    else:
        sys.exit(0)

play = 1
position_list = []
test_board = ['#'] * 10
while play in range(1, 10):
    player_input(play, test_board)
    play += 1
