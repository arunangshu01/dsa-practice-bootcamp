"""

LeetCode Question: 58. Length of Last Word

"""

import re


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleaned_string = re.sub(r'\s+', ' ', s)
        cleaned_string = re.sub(r'^\s+|\s+$', '', s)
        str_list = cleaned_string.split(' ')
        last_ele_len = len(str_list[-1])
        return last_ele_len
