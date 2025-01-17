"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l,r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                res = max((prices[r]-prices[l]), res)
                r+=1
        return res

sol = Solution()
print(sol.maxProfit([10,1,5,6,7,1]))
