def is_valid(board, r, c, n):
    for i in range(9):
        if board[r][i] == n or board[i][c] == n:
            return False
    start_r, start_c = 3 * (r // 3), 3 * (c // 3)
    for i in range(3):
        for j in range(3):
            if board[start_r + i][start_c + j] == n:
                return False
    return True
def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for n in range(1, 10):
                    if is_valid(board, r, c, n):
                        board[r][c] = n
                        if solve(board): return True
                        board[r][c] = 0
                return False
    return True
def print_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else '.' for x in row))
def input_board():
    return [list(map(int, input(f"Row {i+1}: ").split())) for i in range(9)]
if __name__ == "__main__":
    board = input_board()
    if solve(board):
        print("Solved Sudoku:")
        print_board(board)
    else:
        print("No solution exists")
