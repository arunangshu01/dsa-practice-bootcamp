"""

LeetCode Question: 326. Power of Three

"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            while n != 1:
                if n % 3 != 0:
                    return False
                else:
                    n = n // 3
            return True
