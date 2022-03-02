from typing import List

# 0 = 0
# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 5
class Solution:
    def climbStairs(self, n: int) -> int:
      first, second = 0, 1

      for i in range(n):
        first, second = second, first+second
      return second

sol = Solution()
print(sol.climbStairs(5))
