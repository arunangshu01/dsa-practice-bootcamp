"""

LeetCode Question: 217. Contains Duplicate

"""


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurences = {}
        for item in nums:
            if item not in occurences:
                occurences[item] = 1
            else:
                occurences[item] += 1

        result = False

        for key in occurences:
            if occurences[key] > 1:
                result = True
                break
            continue

        return result
