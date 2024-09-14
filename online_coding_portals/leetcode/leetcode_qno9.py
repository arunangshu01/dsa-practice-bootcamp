"""

Leetcode Question: 9. Palindrome Number

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            temp , reverse = x, 0
            while temp != 0:
                remainder = temp % 10
                reverse = (reverse * 10) + remainder
                temp = temp // 10
            if reverse == x:
                return True
            return False
