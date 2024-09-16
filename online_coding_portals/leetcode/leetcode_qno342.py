"""

LeetCode Question: 342. Power of Four

"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        while n % 4 == 0:
            n /= 4
        if n == 1:
            return True
        return False
