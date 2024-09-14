"""

LeetCode Question:  1672. Richest Customer Wealth

"""


from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_list, max_wealth = [], 0
        for account in accounts:
            wealth_list.append(sum(account))
        max_wealth = wealth_list[0]
        for i in range(len(wealth_list)):
            if max_wealth < wealth_list[i]:
                max_wealth = wealth_list[i]
        return max_wealth
