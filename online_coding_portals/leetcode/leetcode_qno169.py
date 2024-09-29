"""

LeetCode Question: 169. Majority Element

"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size, count_dict, majority_element = len(nums), {}, 0
        for item in nums:
            if item not in count_dict:
                count_dict[item] = 1
            else:
                count_dict[item] += 1

        for key in count_dict:
            if count_dict[key] > int(size / 2):
                majority_element = key
        return majority_element
