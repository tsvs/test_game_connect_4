import numpy as np

N_ROWS = 6
N_COLUMNS = 7
N_PLAYERS = 2


def create_board():
    board = np.zeros((N_ROWS, N_COLUMNS))
    return board


def is_valid_input(player_input):
    try:
        number = int(player_input)
        return number < N_COLUMNS

    except:
        return False


def player_move(board, row, column, piece):
    board[row][column] = piece


def is_valid_slot(board, column):
    # if this true -> allow the move
    return board[N_ROWS - 1][column] == 0


def get_free_row(board, column):
    for r in range(N_ROWS):
        if board[r][column] == 0:
            return r


def check(board, player):
    # Check for horizontal
    for c in range(N_COLUMNS - 3):
        for r in range(N_ROWS):
            if board[r][c] == player \
                    and board[r][c + 1] == player \
                    and board[r][c + 2] == player\
                    and board[r][c + 3] == player:
                return True

    # Check for vertical
    for c in range(N_COLUMNS):
        for r in range(N_ROWS - 3):
            if board[r][c] == player \
                    and board[r + 1][c] == player \
                    and board[r + 2][c] == player \
                    and board[r + 3][c] == player:
                return True

    # Check for raising diagonals
    for c in range(N_COLUMNS - 3):
        for r in range(N_ROWS - 3):
            if board[r][c] == player \
                    and board[r + 1][c + 1] == player \
                    and board[r + 2][c + 2] == player\
                    and board[r + 3][c + 3] == player:
                return True

    # Check for falling diagonals
    for c in range(N_COLUMNS - 3):
        for r in range(3, N_ROWS):
            if board[r][c] == player \
                    and board[r - 1][c + 1] == player \
                    and board[r - 2][c + 2] == player \
                    and board[r - 3][c + 3] == player:
                return True


def display_game(board):
    # print(board)
    print(np.flip(board, 0))


win = False
game_board = create_board()
display_game(game_board)

while not win:
    # input from player
    for player in range(1, N_PLAYERS+1):
        valid = False

        col = int(input(f"Player - {player}, turn! options: 0 - {N_COLUMNS}: "))

        # Player's move
        if is_valid_slot(game_board, col):
            row = get_free_row(game_board, col)
            player_move(game_board, row, col, player)
            if check(game_board, player):
                win = True
                print(f"player number {player} has won!")
                display_game(game_board)
                break

        else:
            print('full column, choose another one')
            # TODO: need to fix here (return to current player turn)

        display_game(game_board)



