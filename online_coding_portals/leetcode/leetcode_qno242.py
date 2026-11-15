"""
LeetCode Question: 242. Valid Anagram

Difficulty: Easy
Source: LeetCode
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False
