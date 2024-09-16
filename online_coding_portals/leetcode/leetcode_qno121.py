"""

LeetCode Question: 121. Best Time to Buy and Sell Stock

"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            current_profit = prices[i] - min_price
            max_profit = max(current_profit, max_profit)
            min_price = min(min_price, prices[i])

        return max_profit
