class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            if i > n:
                return 0
            
            one = dfs(i+1)
            two = dfs(i+2)

            memo[i] = one+two

            return one+two

        return dfs(0)
        
