class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one, two = 0, 1
        maxProfit = 0

        # move left ptr if right ptr is less (buy low)
        while two < len(prices):
            maxProfit = max(maxProfit, prices[two] - prices[one])
            if prices[two] < prices[one]:
                one = two
            two += 1

        return maxProfit
