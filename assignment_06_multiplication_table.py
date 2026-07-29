# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def generate_single_table(n):
    """Generates and prints the multiplication table for a given number N from 1 to 12."""
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")


def generate_multiple_tables(n):
    """Generates multiplication tables for every number from 1 to N."""
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    for num in range(1, n + 1):
        generate_single_table(num)
        if num < n:
            print("-----------------------------------")


def main():
    print("=== PART A - Single Table ===")
    try:
        n_input = input("Enter a number: ")
        n = int(n_input)
        if n <= 0:
            print("Error: N must be a positive integer.")
            return
        generate_single_table(n)
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")
        return

    print("\n" + "=" * 35)
    print("=== PART B - Tables from 1 to N ===")
    try:
        n_bonus_input = input("Enter a number N: ")
        n_bonus = int(n_bonus_input)
        if n_bonus <= 0:
            print("Error: N must be a positive integer.")
            return
        generate_multiple_tables(n_bonus)
    except ValueError:
        print("Error: Invalid input. Please enter a positive integer.")


if __name__ == "__main__":
    main()
