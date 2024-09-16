"""

LeetCode Question: 125. Valid Palindrome
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_str = ""
        palindrome = True

        for i in range(len(s)):
            if s[i].isalnum():
                refined_str += s[i]

        refined_str = refined_str.lower()
        rev_refined_str = refined_str[::-1]

        if refined_str == rev_refined_str:
            return True
        return False