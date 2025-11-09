def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row, n):
    if row >= n:
        print("Final N-Queens Matrix:")
        print_board(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = 0

    return False

def nqueens_with_first_fixed(n, first_row, first_col):
    board = [[0] * n for _ in range(n)]
    board[first_row][first_col] = 1
    if not solve_nqueens(board, first_row + 1, n):
        print("No solution exists.")

if __name__ == "__main__":
    n = int(input("Enter n: "))
    r = int(input("Enter first queen row (0-indexed): "))
    c = int(input("Enter first queen col (0-indexed): "))
    nqueens_with_first_fixed(n, r, c)
