#!/usr/bin/python3
'''
A script that returns a list of lists
that represent Pascal's Triangle
'''


def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        new_row = []
        if not triangle:
            new_row.append(1)
            triangle.append(new_row)
        else:
            upper_row = triangle[-1]
            if len(upper_row) == 1:
                new_row.extend([upper_row[0], upper_row[0]])
            else:
                for idx in range(len(upper_row)):
                    if idx == 0:
                        new_row.append(1)
                    else:
                        new_row.append(upper_row[idx - 1] + upper_row[idx])
                new_row.append(1)
            triangle.append(new_row)
    return triangle
