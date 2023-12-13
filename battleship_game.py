import random

# Initialize constants
BOARD_SIZE = 5
SHIP_COUNT = 3

# Initialize boards
player_board = [['O'] * BOARD_SIZE for _ in range(BOARD_SIZE)]
opponent_board = [['O'] * BOARD_SIZE for _ in range(BOARD_SIZE)]
opponent_view = [['O'] * BOARD_SIZE for _ in range(BOARD_SIZE)]

# Function to print board state
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Function to place ships
def place_ships(board):
    for _ in range(SHIP_COUNT):
        x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
        while board[x][y] == 'S':
            x, y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
        board[x][y] = 'S'

# Function to take a turn
def take_turn(board, view):
    print("Enter coordinates (row, column) for your shot:")
    x, y = map(int, input().split())
    if board[x][y] == 'S':
        print("Hit!")
        view[x][y] = 'H'
        board[x][y] = 'H'
    else:
        print("Miss!")
        view[x][y] = 'X'

# Check for win condition
def check_win(board):
    for row in board:
        if 'S' in row:
            return False
    return True

# Main game loop
def play_game():
    place_ships(opponent_board)
    turns = 0

    while True:
        print("Player's board:")
        print_board(player_board)
        print("Opponent's board:")
        print_board(opponent_view)

        take_turn(opponent_board, opponent_view)
        turns += 1

        if check_win(opponent_board):
            print("All opponent's ships have been sunk! You win!")
            print(f"It took you {turns} turns.")
            break

# Start the game
play_game()
