"""

LeetCode Question: 28. Find the Index of the First Occurrence in a String

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        output = 0

        if haystack.__contains__(needle):
            output = haystack.index(needle)
        else:
            output = -1

        return output
