#!/usr/bin/python3
"""
0-main
"""

def pascal_triangle(n):
    """
    pascal triangle
    """
    result = [[1]]
    if n < 0:
        return []

    while len(result) < n:
        previous = result[-1]
        current = [1]

        for i in range(1, len(previous)):
            current.append(previous[i-1] + previous[i])
            
        current.append(1)
        result.append(current)
    return result