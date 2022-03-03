from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      if amount == 0:
        return 0

      total = 0
      cur_index = 0
      ctr = 0
      coins.sort(reverse=True)
      print(coins)
      print(coins[cur_index]%amount)

      if len(coins) == 1 and amount%coins[cur_index] != 0:
        print('mod')
        return -1

      while total < amount:
        print(total)
        print(cur_index)
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
print(sol.coinChange([186,419,83,408] , 6249))
