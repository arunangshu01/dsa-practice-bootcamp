"""

LeetCode Question:  1. Two Sum

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in visited:
                return [visited[comp], i]
            visited[num] = i
        return [None, None]
