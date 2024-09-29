"""

LeetCode Question: 383. Ransom Note

"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            rn_char = ransomNote[i]
            if rn_char in magazine:
                match_index = magazine.index(rn_char)
            else:
                match_index = -1

            if match_index == -1:
                return False

            magazine = magazine[0:match_index] + magazine[match_index + 1:]
        return True
