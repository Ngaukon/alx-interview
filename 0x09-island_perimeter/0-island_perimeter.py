#!/usr/bin/python3
"""Island Perimeter Problem
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    Args:
        grid: 2D list with 0 (water) and 1 (land).
    Returns:
        Perimeter of the island.
    """
    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check top
                if i <= 0 or grid[i - 1][j] == 0:
                    p += 1
                # Check bottom
                if i >= len(grid) - 1 or grid[i + 1][j] == 0:
                    p += 1
                # Check left
                if j <= 0 or grid[i][j - 1] == 0:
                    p += 1
                # Check right
                if j >= len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    p += 1
    return p
