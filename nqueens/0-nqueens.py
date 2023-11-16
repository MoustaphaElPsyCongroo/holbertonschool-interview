#!/usr/bin/python3
"""Partial N queens puzzle challenge"""
from sys import argv


def is_placeable(current_positions, x, y):
    """Checks if a queen can be placed in the specified row:col combination"""
    for queen in current_positions:
        queen_x = queen[0]
        queen_y = queen[1]

        # Rule out x lines and y columns
        if x == queen_x or y == queen_y:
            return False

        # Rule out remaining diagonals
        if y - x == queen_y - queen_x or y + x == queen_x + queen_y:
            return False
    return True


def place_queens(n):
    """Places n queens on a n sized board, column by column. Checks 'almost'
    each square of a column for placeable queens, skipping the rest of squares
    when a queen is successfully placed. If no queen can be placed on an entire
    column due to the current placement, backtracks to check from the last
    valid one for an alternative placement."""
    for starting_col in range(1, n):
        board = []
        y = starting_col
        # print("line:", starting_col)
        x = 0
        while x < n:
            while y < n:
                # print(board)
                # print(x, y)
                if is_placeable(board, x, y):
                    board.append([x, y])
                    break
                y += 1
            else:
                # print("backtracking")
                last_valid = board.pop()

                if len(board) == 0:
                    break

                x = last_valid[0]
                y = last_valid[1] + 1
                continue
            x += 1
            y = 0
        if board:
            print(board)


def validate_command():
    """Validates that the user correctly called the program"""
    if len(argv) < 2:
        print("Usage: nqueens N")
        exit(1)

    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    else:
        n = int(argv[1])

    if n < 4:
        print("N must be at least 4")
        exit(1)

    return n


def main():
    """Entry point"""
    n = validate_command()
    place_queens(n)


if __name__ == "__main__":
    main()
