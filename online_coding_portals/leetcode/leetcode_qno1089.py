"""

LeetCode Question: 1089. Duplicate Zeros

"""

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_new = [item for item in arr]
        i = 0
        j = 0
        while i < len(arr):
            if arr_new[j] == 0:
                arr[i] = 0
                i = i + 1
                if i < len(arr):
                    arr[i] = 0
            else:
                arr[i] = arr_new[j]
            i = i + 1
            j = j + 1
        print(arr)
