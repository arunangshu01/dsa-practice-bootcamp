"""

LeetCode Question: 66. Plus One

"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ''.join(str(digit) for digit in digits)
        digit = int(digits_str) + 1
        digit_str = str(digit)
        digit_list = list(digit_str)
        digit_list = [int(item) for item in digit_list]
        return digit_list
