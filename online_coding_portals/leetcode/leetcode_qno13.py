"""

LeetCode Question: 13. Roman to Integer

"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number_list, integer_number = [], 0

        for i in range(len(s)):
            number_list.append(roman_map[s[i]])

        for i in range(0, len(number_list) - 1):
            if number_list[i] < number_list[i + 1]:
                integer_number -= number_list[i]
            else:
                integer_number += number_list[i]

        integer_number += number_list[-1]
        return integer_number
