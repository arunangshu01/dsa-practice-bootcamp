"""

2D Lists

Given 2D list calculate the sum of diagonal elements.

Example:
    myList2D= [[1,2,3],[4,5,6],[7,8,9]]
    diagonal_sum(myList2D) # 15

"""


def diagonal_sum(matrix):
    sum_diag = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                sum_diag += matrix[i][j]
    return sum_diag


def diagonal_sum_new(matrix):
    sum_diag = 0
    for i in range(len(matrix)):
        sum_diag += matrix[i][i]
    return sum_diag


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    result1 = diagonal_sum(matrix=matrix)
    result2 = diagonal_sum_new(matrix=matrix)
    print(result1)
    print(result2)
