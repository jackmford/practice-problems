class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [-1]*len(cost)
        def dfs(i):
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]

            left = dfs(i+1)
            right = dfs(i+2)

            memo[i] = cost[i] + min(left, right)

            return cost[i] + min(left, right)
            

        res = min(dfs(0), dfs(1))

        return res

            
        
