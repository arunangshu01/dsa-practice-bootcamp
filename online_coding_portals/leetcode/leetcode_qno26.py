"""
LeetCode Question: 26. Remove Duplicates from Sorted Array

Difficulty: Easy
Source: LeetCode
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[count] = nums[i]
                count += 1
        return count
