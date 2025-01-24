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
            
