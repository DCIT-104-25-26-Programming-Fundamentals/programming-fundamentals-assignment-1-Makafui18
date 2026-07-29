# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def input_matrix(rows, cols, name="Matrix"):
    """Helper function to read a matrix from user input row by row."""
    matrix = []
    print(f"\nEntering values for {name} ({rows}x{cols}):")
    for i in range(rows):
        while True:
            row_str = input(f"Enter row {i + 1}: ").strip()
            row = [float(val) for val in row_str.split()]
            if len(row) == cols:
                matrix.append(row)
                break
            print(f"Error: Please enter exactly {cols} numbers separated by spaces.")
    return matrix


def display_matrix(matrix):
    """Helper function to display a 2D matrix in a clean, aligned grid format."""
    for row in matrix:
        print("  ".join(f"{int(val) if val.is_integer() else val:>4}" for val in row))


def transpose_matrix(matrix):
    """Computes and returns the transpose of a given matrix (rows -> columns)."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
        
    return transposed


def add_matrices(matrix_a, matrix_b):
    """Computes and returns element-wise sum of two matrices of identical dimensions."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    
    for i in range(rows):
        row_sum = []
        for j in range(cols):
            row_sum.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row_sum)
        
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Computes and returns the matrix product A x B (M x N multiplied by N x P = M x P)."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    result = []
    for i in range(rows_a):
        row_result = []
        for j in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum += matrix_a[i][k] * matrix_b[k][j]
            row_result.append(cell_sum)
        result.append(row_result)
        
    return result


def main():
    print("=== PART A: Transpose a Matrix ===")
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    mat = input_matrix(r, c, "Matrix")
    
    print("\nOriginal Matrix:")
    display_matrix(mat)
    
    print("\nTransposed Matrix:")
    display_matrix(transpose_matrix(mat))
    
    print("\n" + "="*35)
    print("=== PART B: Add Two Matrices ===")
    r_add = int(input("Enter number of rows: "))
    c_add = int(input("Enter number of columns: "))
    mat_a = input_matrix(r_add, c_add, "Matrix A")
    mat_b = input_matrix(r_add, c_add, "Matrix B")
    
    print("\nSum Matrix (A + B):")
    display_matrix(add_matrices(mat_a, mat_b))
    
    print("\n" + "="*35)
    print("=== PART C: Multiply Two Matrices ===")
    r_m1 = int(input("Enter rows for Matrix A: "))
    c_m1 = int(input("Enter columns for Matrix A (and rows for Matrix B): "))
    c_m2 = int(input("Enter columns for Matrix B: "))
    
    mat_mult_a = input_matrix(r_m1, c_m1, "Matrix A")
    mat_mult_b = input_matrix(c_m1, c_m2, "Matrix B")
    
    print("\nProduct Matrix (A x B):")
    display_matrix(multiply_matrices(mat_mult_a, mat_mult_b))


if __name__ == "__main__":
    main()