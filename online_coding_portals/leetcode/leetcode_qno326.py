"""

LeetCode Question: 326. Power of Three

"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        return False
