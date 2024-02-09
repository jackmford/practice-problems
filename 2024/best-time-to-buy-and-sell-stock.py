from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 
        maxPrice = 0

        while r < len(prices):
             if prices[r] < prices[l]:
                 l = r
             if prices[r] - prices[l] > maxPrice:
                 maxPrice = prices[r] - prices[l]
             r += 1
            
        return maxPrice

sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))