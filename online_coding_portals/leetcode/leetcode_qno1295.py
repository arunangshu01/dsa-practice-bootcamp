"""

Leetcode Question: 1295. Find Numbers with Even Number of Digits

"""

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        str_nums = [str(num) for num in nums]
        len_nums = [len(str_num) for str_num in str_nums]
        even = 0
        for length in len_nums:
            if length % 2 == 0:
                even += 1
        return even
