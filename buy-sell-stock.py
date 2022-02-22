from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    cur_lowest = prices[0]
    for i in range(1, len(prices)):
      if prices[i] < cur_lowest:
        cur_lowest = prices[i]
      if prices[i]-cur_lowest > max_profit:
        max_profit = prices[i]-cur_lowest

    return max_profit

sol = Solution()
num = sol.maxProfit([7, 1, 5, 3, 6, 4])
print(num)
