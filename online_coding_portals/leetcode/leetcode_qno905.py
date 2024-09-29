"""

LeetCode Question: 905. Sort Array By Parity

"""

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for item in nums:
            if item % 2 == 0:
                even.append(item)
            else:
                odd.append(item)
        even.sort()
        odd.sort()
        final = even + odd
        return final
