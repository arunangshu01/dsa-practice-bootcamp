"""

LeetCode Question: 303. Range Sum Query - Immutable

"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum_range = 0
        while left <= right:
            sum_range += self.nums[left]
            left += 1
        return sum_range

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
