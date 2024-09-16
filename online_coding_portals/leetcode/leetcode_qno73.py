"""

LeetCode Question: 73. Set Matrix Zeroes

"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_idx, col_idx = [], []
        row_length, col_length = len(matrix), len(matrix[0])
        for i in range(row_length):
            for j in range(col_length):
                if matrix[i][j] == 0:
                    row_idx += [i]
                    col_idx += [j]

        for i in range(row_length):
            for j in range(col_length):
                if i in row_idx or j in col_idx:
                    matrix[i][j] = 0
