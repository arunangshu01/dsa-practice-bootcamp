"""

LeetCode Question: 136. Single Number

"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occurrances = {}
        for i in range(len(nums)):
            if nums[i] not in occurrances:
                occurrances[nums[i]] = 1
            else:
                occurrances[nums[i]] += 1

        for key in occurrances:
            if occurrances[key] == 1:
                return key
