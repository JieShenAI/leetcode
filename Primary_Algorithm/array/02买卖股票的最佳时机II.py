from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        stock = prices[0]
        profit = 0
        for i in range(0, len(prices)-1):
            # stock will increase,tomorrow
            if prices[i+1] > prices[i]:
                # just buy it
                if stock == -1:
                    stock = prices[i]
                continue
            # stock will decrease,sell it
            if stock != -1:
                profit += prices[i] - stock
                stock = -1
        if stock != -1:
            profit += prices[-1] - stock
        return profit
