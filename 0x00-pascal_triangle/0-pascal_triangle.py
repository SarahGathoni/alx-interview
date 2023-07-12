#!/usr/bin/python3
""" a function that creates the Pascal's triangle"""


def pascal_triangle(n):
    """Pascal's triangle function"""
    triangle_list = [[1]]
    for i in range(1, n):
        row = [1] + [triangle_list[i-1][j] + triangle_list[i-1][j+1] for j in range(i-1)] + [1]
        triangle_list.append(row)
    return triangle_list if n > 0 else []    
