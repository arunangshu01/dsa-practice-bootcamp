"""

LeetCode Question: 119. Pascal's Triangle II

"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1] * (i + 1) for i in range(rowIndex + 2)]
        for i in range(2, rowIndex + 2):
            for j in range(1, i):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        return triangle[rowIndex]
