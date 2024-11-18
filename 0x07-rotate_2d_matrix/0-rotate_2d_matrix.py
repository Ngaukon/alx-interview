#!/usr/bin/python3
"""2D matrix rotation module."""

def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in place."""
    if type(matrix) != list:  # Ensure input is a list.
        return
    if len(matrix) <= 0:  # Ensure matrix is not empty.
        return
    if not all(map(lambda x: type(x) == list, matrix)):  # Ensure all rows are lists.
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):  # Ensure all rows are of equal length.
        return
    c, r = 0, rows - 1  # Initialize column and row counters.
    for i in range(cols * rows):  # Iterate through all elements.
        if i % rows == 0:  # Start a new row in the rotated matrix.
            matrix.append([])
        if r == -1:  # Reset row counter when it reaches the top.
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])  # Add element to rotated matrix.
        if c == cols - 1 and r >= -1:  # Remove processed rows.
            matrix.pop(r)
        r -= 1  # Move to the next row upwards.
