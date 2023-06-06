from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    #max_profit = 0
    #cur_lowest = prices[0]
    #for i in range(1, len(prices)):
    #  if prices[i] < cur_lowest:
    #    cur_lowest = prices[i]
    #  if prices[i]-cur_lowest > max_profit:
    #    max_profit = prices[i]-cur_lowest

    #return max_profit

    # review
    left_ptr = 0
    right_ptr = 1
    cur_profit = 0

    while right_ptr <= len(prices)-1:
      if prices[right_ptr] < prices[left_ptr]:
        left_ptr = right_ptr
      elif prices[right_ptr] - prices[left_ptr] > cur_profit:
        cur_profit = prices[right_ptr] - prices[left_ptr]
      
      right_ptr += 1
    
    return cur_profit




sol = Solution()
num = sol.maxProfit([7, 1, 5, 3, 6, 4])
print(num)
