"""
LeetCode Question: 33. Search in Rotated Sorted Array

Source: LeetCode
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
