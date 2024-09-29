"""

LeetCode Question: 69. Sqrt(x)

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        sqrtNum = x / 2
        temp = 0
        while sqrtNum != temp:
            temp = sqrtNum
            sqrtNum = (x / temp + temp) / 2
        return int(sqrtNum)
