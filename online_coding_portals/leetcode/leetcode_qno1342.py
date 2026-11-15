"""
LeetCode Question:  1342. Number of Steps to Reduce a Number to Zero

Difficulty: Easy
Source: LeetCode
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            steps += 1
        return steps
