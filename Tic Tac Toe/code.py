#tictactoe
import random

def create_board():
    return [[' ']*3 for _ in range(3)]
def is_board_filled(board):
    return all(' ' not in row for row in board)
def check_win(board, player):
    win_conditions = (
        [all(mark == player for mark in row) for row in board] +  # Check rows
        [all(board[row][col] == player for row in range(3)) for col in range(3)] +  # Check columns
        [all(board[i][i] == player for i in range(3)),  # Check main diagonal
        all(board[i][2-i] == player for i in range(3))]  # Check anti-diagonal
    )
    return any(win_conditions)
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-+-+-')
    print()  # Extra line for better readability
def start_game():
    board = create_board()
    current_player = random.choice(['X', 'O'])
    print(f"Player {current_player} starts the game.")
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn: ")
        try:
            row, col = map(int, input("Enter row and column number (0-2) separated by space: ").split())
        except ValueError:
            print("Invalid input. Please enter numbers separated by space.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid move. Please enter numbers between 0 and 2.")
            continue

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
