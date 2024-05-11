import random

# Function to print the Tic Tac Toe board
def print_board(board):
    print('-------------')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('-------------')

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to get available moves
def get_available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']

# Minimax algorithm for AI player
def minimax(board, depth, maximizing_player):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth+1, False)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth+1, True)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

# Function to get AI's move using Minimax
def get_ai_move(board):
    best_move = None
    best_eval = float('-inf')
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        eval = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# Main function to play the game
# Main function to play the game
def play_tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's move
        row, col = map(int, input("Enter your move (row col): ").split())
        row -= 1  # Adjusting for 0-based indexing
        col -= 1  # Adjusting for 0-based indexing
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI is thinking...")
        ai_row, ai_col = get_ai_move(board)
        board[ai_row][ai_col] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

play_tic_tac_toe()
