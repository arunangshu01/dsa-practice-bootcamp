"""

LeetCode Question: 414. Third Maximum Number

"""

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = []
        for item in nums:
            if item not in unique:
                unique.append(item)
        if len(unique) < 3:
            third_max = max(unique)
        else:
            unique.sort(reverse=True)
            third_max = unique[2]

        return third_max
