class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #memo = [[-1] * (amount) for _ in range(len(coins))]
        coins.sort()
        memo = {}
        def dfs(i, total):
            if amount == total:
                return 1
            if i >= len(coins):
                return 0
            if (i, total) in memo:
                return memo[(i, total)]

            res = 0
            if coins[i]+total <= amount:
                # Skip number
                res = dfs(i+1, total)
                # Use number
                res += dfs(i, total+coins[i])

            memo[(i, total)] = res
            return res

        return dfs(0, 0)
            
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # At any i you can take i again and add to total
        # Or you can move i and  
        #memo = {}
        memo = [[-1]*(amount) for _ in range(len(coins))]
        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if i >= len(coins):
                return 0
            if memo[i][total] != -1:
                return memo[i][total]
            
            res = 0 
            res += dfs(i+1, total)
            res += dfs(i, total+coins[i])

            memo[i][total] = res
            return memo[i][total]

        return dfs(0, 0)
