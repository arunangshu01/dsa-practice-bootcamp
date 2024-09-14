"""

LeetCode Question:  1480. Running Sum of 1d Array

"""


from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list, sum_value = [], 0
        for i in range(len(nums)):
            sum_value += nums[i]
            sum_list.append(sum_value)
        return sum_list
