#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    '''Generates a list of lists representing Pascal's triangle 
    up to a specified number of rows.
    
    Args:
        n (int): The number of rows in the Pascal's triangle.
        
    Returns:
        list: A list of lists containing integers representing 
        the rows of Pascal's triangle. Returns an empty list if 
        the input is not a positive integer.
    '''
    triangle = []  # Initialize an empty list to hold the triangle's rows
    if type(n) is not int or n <= 0:
        return triangle  # Return an empty list for invalid input
    for i in range(n):
        line = []  # Initialize an empty list to hold the current row
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)  # The first and last elements of each row are 1
            elif i > 0 and j > 0:
                # Each inner element is the sum of the two elements above it
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)  # Add the current row to the triangle
    return triangle  # Return the complete Pascal's triangle
