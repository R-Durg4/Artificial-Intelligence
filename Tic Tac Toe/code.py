#tictactoe
import random

def create_board():
    return [[' ']*3 for _ in range(3)]

def is_board_filled(board):
    return all(' ' not in row for row in board)

def check_win(board, player):
    win_conditions = (
        all(mark == player for mark in row) for row in board) \
        | (all(board[row][col] == player for row in range(3)) for col in range(3)) \
        | (all(board[i][i] == player for i in range(3))) \
        | (all(board[i][2-i] == player for i in range(3)))
    return any(win_conditions)

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-+-+-')

def start_game():
    board = create_board()
    current_player = random.choice(['X', 'O'])
    print(f"Player {current_player} starts the game.")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn: ")
        row, col = map(int, input("Enter row and column number (0-2) separated by space: ").split())

        if board[row][col] != ' ':
            print("Spot already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_filled(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

if __name__ == "__main__":
    start_game()
