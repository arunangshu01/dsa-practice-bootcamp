"""

LeetCode Question: 14. Longest Common Prefix

"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            lc_prefix = ""
            return lc_prefix
        lc_prefix = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            if len(lc_prefix) == 0:
                break
            for j in range(0, len(strs[i])):
                if j < len(lc_prefix) and lc_prefix[j] == strs[i][j]:
                    temp += lc_prefix[j]
                else:
                    break
            lc_prefix = temp
        return lc_prefix
