"""

LeetCode Question: 941. Valid Mountain Array

"""

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        if arr_len < 3:
            return False
        else:
            left_index, right_index = 0, arr_len - 1
            while left_index < arr_len - 1 and arr[left_index] < arr[left_index + 1]:
                left_index += 1

            while right_index > 0 and arr[right_index - 1] > arr[right_index]:
                right_index -= 1

            if left_index > 0 and left_index == right_index and right_index < arr_len - 1:
                return True
            return False
