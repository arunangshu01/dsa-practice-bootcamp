"""

LeetCode Question: 4. Median of Two Sorted Arrays

"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = nums1 + nums2
        merged_list.sort()
        if len(merged_list) % 2 == 0:
            first_middle = len(merged_list) // 2
            second_middle = first_middle + 1
            median = (merged_list[first_middle - 1] + merged_list[second_middle - 1]) / 2
        else:
            middle = len(merged_list) // 2
            median = merged_list[middle]
        return median
