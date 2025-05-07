def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_backtracking(board, row, n):
    if row == n:
        # Print solution
        for r in board:
            print(" ".join("Q" if x == 1 else "." for x in r))
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_backtracking(board, row + 1, n)
            board[row][col] = 0  # Backtrack

# Main
n = int(input("Enter value of N for N-Queens: "))
board = [[0 for _ in range(n)] for _ in range(n)]
print("\nSolutions using Backtracking:")
solve_n_queens_backtracking(board, 0, n)

def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] else ".", end=" ")
        print()
    print()

def solve_n_queens_bnb(row, n, board, cols, diag1, diag2):
    if row == n:
        print_solution(board, n)
        return True  # Change to False to print all solutions

    for col in range(n):
        d1 = row - col + n - 1
        d2 = row + col
        if not cols[col] and not diag1[d1] and not diag2[d2]:
            board[row][col] = 1
            cols[col] = diag1[d1] = diag2[d2] = True

            if solve_n_queens_bnb(row + 1, n, board, cols, diag1, diag2):
                return True  # return True to print only one solution

            # Backtrack
            board[row][col] = 0
            cols[col] = diag1[d1] = diag2[d2] = False
    return False

# Main program
n = int(input("Enter value of N for N-Queens: "))
board = [[0] * n for _ in range(n)]
cols = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

print("\nBranch and Bound solution:")
if not solve_n_queens_bnb(0, n, board, cols, diag1, diag2):
    print("No solution exists for this N.")
