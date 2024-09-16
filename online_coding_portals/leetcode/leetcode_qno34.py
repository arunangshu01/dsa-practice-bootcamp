"""

LeetCode Question: 34. Find First and Last Position of Element in Sorted Array

"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_index, second_index = 0, 0
        if len(nums) == 0:
            first_index, second_index = -1, -1
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    first_index = i
                    break
                else:
                    first_index = -1

            for j in range(len(nums) - 1, -1, -1):
                if nums[j] == target:
                    second_index = j
                    break
                else:
                    second_index = -1

        return [first_index, second_index]
