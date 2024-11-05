#!/usr/bin/python3
"""Module to find solutions for the N queens problem.
"""
import sys


solutions = []
"""List to store all possible solutions to the N queens problem.
"""
n = 0
"""Integer representing the size of the chessboard (N).
"""
pos = None
"""List of possible positions on the chessboard represented as coordinates.
"""


def get_input():
    """Retrieves and validates the command-line argument for the chessboard size.

    Returns:
        int: The size of the chessboard (N).
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")  # Prompt for correct usage if argument count is incorrect
        sys.exit(1)
    try:
        n = int(sys.argv[1])  # Attempt to convert the argument to an integer
    except Exception:
        print("N must be a number")  # Error message if conversion fails
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")  # Error message if N is less than 4
        sys.exit(1)
    return n  # Return the validated chessboard size


def is_attacking(pos0, pos1):
    """Checks if two queens positioned at pos0 and pos1 can attack each other.

    Args:
        pos0 (list or tuple): The position of the first queen as (row, column).
        pos1 (list or tuple): The position of the second queen as (row, column).

    Returns:
        bool: True if the queens can attack each other, otherwise False.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True  # Same row or column means they can attack
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])  # Check diagonal attack


def group_exists(group):
    """Checks if a specific configuration of queens exists in the list of solutions.

    Args:
        group (list of integers): A configuration of queen positions.

    Returns:
        bool: True if the configuration exists in the solutions, otherwise False.
    """
    global solutions
    for stn in solutions:  # Iterate through existing solutions
        i = 0
        for stn_pos in stn:  # Check each position in the current solution
            for grp_pos in group:  # Check against the new group of positions
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:  # Compare positions
                    i += 1  # Count matches
        if i == n:  # If all positions match
            return True  # The group already exists
    return False  # No match found


def build_solution(row, group):
    """Recursively builds a valid solution for the N queens problem.

    Args:
        row (int): The current row being evaluated on the chessboard.
        group (list of lists of integers): The current group of valid positions.
    """
    global solutions
    global n
    if row == n:  # If all rows have been placed successfully
        tmp0 = group.copy()  # Make a copy of the current group
        if not group_exists(tmp0):  # Check if the solution already exists
            solutions.append(tmp0)  # Store the valid solution
    else:
        for col in range(n):  # Iterate through each column in the current row
            a = (row * n) + col  # Calculate the index in the flat position list
            matches = zip(list([pos[a]]) * len(group), group)  # Pair current position with all group positions
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)  # Check for attacking positions
            group.append(pos[a].copy())  # Add the current position to the group
            if not any(used_positions):  # If no queens are attacking
                build_solution(row + 1, group)  # Recur to the next row
            group.pop(len(group) - 1)  # Backtrack to remove the current position


def get_solutions():
    """Generates all solutions for the N queens problem given the chessboard size.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))  # Create a list of positions on the chessboard
    a = 0
    group = []  # Initialize an empty group for valid positions
    build_solution(a, group)  # Start building solutions from the first row


n = get_input()  # Get the validated input for chessboard size
get_solutions()  # Generate the solutions based on the input size
for solution in solutions:  # Print each found solution
    print(solution)  # Output the solution as a list of queen positions
