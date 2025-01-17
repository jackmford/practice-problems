class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # What is the simple recursion?
        # Try every path
        memo = {}
        
        def dfs(total):
            # already computed this sub problem
            if total in memo:
                return memo[total]
            if total >= amount:
                # We have enough coins
                return 0

            res = float("inf")
            # At each level we can choose *any* coin
            for coin in coins:
                if total+coin <= amount:
                    res = min(res, 1+dfs(total+coin))
            
            memo[total] = res

            return res

        res = dfs(0)
        if res < float("inf"):
            return res
        return -1

