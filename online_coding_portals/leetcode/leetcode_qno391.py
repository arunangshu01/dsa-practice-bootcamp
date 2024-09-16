"""

LeetCode Question: 391. Number of 1 Bits

"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_bits = []
        while n != 1:
            rem = n % 2
            hamming_bits.append(rem)
            n = n // 2
        hamming_bits = hamming_bits[::-1]
        hamming_bits = [n] + hamming_bits
        count = 0
        for item in hamming_bits:
            if item == 1:
                count += 1
        return count
