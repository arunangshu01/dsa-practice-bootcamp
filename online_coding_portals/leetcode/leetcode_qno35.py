"""

Leetcode Question: 35. Search Insert Position

"""


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        if target in nums:
            index = nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            index = nums.index(target)
        return index
