"""
LeetCode Question: 153. Find Minimum in Rotated Sorted Array

Source: LeetCode
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]
        for i in range(len(nums)):
            if min > nums[i]:
                min = nums[i]
        return min
