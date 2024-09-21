"""

LeetCode Question 191: Number of 1 Bits

"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_str, count = "", 0
        while n != 1:
            rem = n % 2
            hamming_str += str(rem)
            n = n // 2
        hamming_str += str(n)
        hamming_str = hamming_str[::-1]
        for char in hamming_str:
            if char == '1':
                count += 1
        return count
