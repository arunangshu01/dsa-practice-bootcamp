"""

LeetCode Question: 7. Reverse Integer

"""


class Solution:
    def reverse(self, x: int) -> int:
        reverse_num = 0
        temp = x
        if temp < 0:
            temp *= -1
        while temp != 0:
            rem = temp % 10
            reverse_num = (reverse_num * 10) + rem
            temp = temp // 10
        if x < 0:
            reverse_num *= -1
        return reverse_num
