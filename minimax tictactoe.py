import itertools
def print_board(board):
    print('\n'.join(' '.join(row) for row in board))
def check_win(board, player):
    return any(all(board[i][j] == player for j in range(3)) for i in range(3)) or \
           any(all(board[i][j] == player for i in range(3)) for j in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3))
def minimax(board, depth, maximizing):
    if check_win(board, 'X'): return 10 - depth
    if check_win(board, 'O'): return depth - 10
    if all(cell != ' ' for row in board for cell in row): return 0
    score = float('-inf') if maximizing else float('inf')
    for i, j in itertools.product(range(3), repeat=2):
        if board[i][j] == ' ':
            board[i][j] = 'X' if maximizing else 'O'
            score = max(score, minimax(board, depth + 1, False)) if maximizing else min(score, minimax(board, depth + 1, True))
            board[i][j] = ' '
    return score
def find_best_move(board):
    best_move, best_score = None, float('-inf')
    for i, j in itertools.product(range(3), repeat=2):
        if board[i][j] == ' ':
            board[i][j] = 'X'
            score = minimax(board, 0, False)
            board[i][j] = ' '
            if score > best_score:
                best_score, best_move = score, (i, j)
    return best_move
board = [[' ']*3 for _ in range(3)]
while True:
    pos = int(input("Enter position for O (1-9): ")) - 1
    if board[pos // 3][pos % 3] == ' ':
        board[pos // 3][pos % 3] = 'O'
        print_board(board)
        if check_win(board, 'O'):
            print("O wins!")
            break
        if all(cell != ' ' for row in board for cell in row):
            print("It's a tie!")
            break
    move = find_best_move(board)
    if move:
        board[move[0]][move[1]] = 'X'
        print_board(board)
        if check_win(board, 'X'):
            print("X wins!")
            break
        if all(cell != ' ' for row in board for cell in row):
            print("It's a tie!")
            break
