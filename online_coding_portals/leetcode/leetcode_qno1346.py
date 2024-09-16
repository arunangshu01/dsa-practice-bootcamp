"""

LeetCode Question: 1346. Check If N and Its Double Exist

"""

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] == arr[j] * 2:
                    return True
                    break
        return False
