"""

LeetCode Question: 1051. Height Checker

"""

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = [item for item in heights]
        expected.sort()
        indices = []
        if len(heights) == len(expected):
            for i in range(len(heights)):
                if heights[i] != expected[i]:
                    indices.append(i)
        return len(indices)
