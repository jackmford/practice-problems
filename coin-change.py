from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      total = 0
      cur_index = 0
      ctr = 0
      coins.sort(reverse=True)
      print(coins)

      if len(coins) == 1 and coins[cur_index] < amount:
        return -1

      while total < amount:
        if total+coins[cur_index] <= amount:
          total+=coins[cur_index]
          ctr+=1
          continue
        cur_index+=1


      if total == amount:
        return ctr
      else:
        return -1

sol = Solution()
print(sol.coinChange([1, 2, 5], 11))
