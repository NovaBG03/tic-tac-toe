import os

emptySymbol = '□'
player1 = '✖'
player2 = 'o'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def init_board():
    board = []
    for i in range(3):
        board.append([emptySymbol, emptySymbol, emptySymbol])
    return board


def print_board(board):
    board_len = len(board)
    first_line = ' '
    for i in range(board_len):
        first_line += ' ' + str(i + 1)
    print(first_line)
    for i in range(board_len):
        print(str(i + 1) + ' ' + ' '.join(board[i]))


def read_position(board):
    row = None
    col = None

    while True:
        input_arr = input('Enter your position (row col): ').split(' ')
        if len(input_arr) != 2:
            print('Please enter 2 numbers')
            continue

        [row, col] = list(map(lambda x: int(x) - 1, input_arr))
        if row < 0 or row >= len(board) or col < 0 or col >= len(board):
            print('Please enter 2 valid numbers')
            continue

        if board[row][col] != emptySymbol:
            print('Please enter an empty position')
            continue
        break
    return [row, col]


def check_winner(board, player):
    for i in range(len(board)):
        is_winning_row = board[i][0] == player and board[i][1] == player and board[i][2] == player
        is_winning_col = board[0][i] == player and board[1][i] == player and board[2][i] == player
        if is_winning_row or is_winning_col:
            return True
    is_winning_diagonal = (board[0][0] == player and board[1][1] == player and board[2][2] == player) or (
                board[0][2] == player and board[1][1] == player and board[2][0] == player)
    return is_winning_diagonal


def start_game():
    board = init_board()

    player = player1
    while True:
        clear()
        print_board(board)
        print('PLAYER ' + player)
        [row, col] = read_position(board)
        board[row][col] = player
        if check_winner(board, player):
            break

        if player == player1:
            player = player2
        else:
            player = player1

    clear()
    print_board(board)
    print('WINNER ' + player)


start_game()
