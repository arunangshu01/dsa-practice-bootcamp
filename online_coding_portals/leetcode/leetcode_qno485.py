"""

LeetCode Question: 485. Max Consecutive Ones

"""


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        string_list = [str(num) for num in nums]
        result_string = ''.join(string_list)
        res_list = result_string.split('0')
        len_list = []
        for item in res_list:
            len_list.append(len(item))
        return max(len_list)
