"""

LeetCode Question: 238. Product of Array Except Self

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length == 1:
            return 0
        left = [0] * length
        right = [0] * length
        prod = [0] * length
        left[0] = 1
        right[length - 1] = 1
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]
        for j in range(length - 2, -1, -1):
            right[j] = nums[j + 1] * right[j + 1]
        for i in range(length):
            prod[i] = left[i] * right[i]
        return prod
