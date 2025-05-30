import math

# Initial empty board
board = [' ' for _ in range(9)]

# Print the game board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for winner
def winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in cond) for cond in win_conditions)

# Check if board is full
def is_full(board):
    return ' ' not in board

# Minimax function
def minimax(board, depth, is_maximizing):
    if winner(board, 'O'):
        return 1
    elif winner(board, 'X'):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Get best move for computer (O)
def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human (X) move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'
        print_board(board)

        if winner(board, 'X'):
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        # Computer (O) move
        print("Computer is making a move...")
        move = best_move()
        board[move] = 'O'
        print_board(board)

        if winner(board, 'O'):
            print("Computer wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

# Run the game
play_game()


