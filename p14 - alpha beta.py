import math

# Initial empty board
board = [' ' for _ in range(9)]

# Print the board
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

# Minimax with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if winner(board, 'O'):
        return 1
    elif winner(board, 'X'):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # β cut-off
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # α cut-off
        return min_eval

# Best move for computer
def best_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe (Alpha-Beta Pruning)!")
    print_board(board)

    while True:
        # Human move
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

        # Computer move
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

# Start game
play_game()
