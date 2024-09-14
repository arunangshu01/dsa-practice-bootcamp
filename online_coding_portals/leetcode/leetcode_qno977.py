"""

Leetcode Question: 977. Squares of a Sorted Array

"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_nums = [num * num for num in nums]
        sq_nums.sort()
        return sq_nums
