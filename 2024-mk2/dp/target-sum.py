class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # For each index i you can add or subtract the number
        # base case if i>=len(nums)
        memo = {}

        def dfs(i, total):
            if i >= len(nums):
                if total == target:
                    return 1
                return 0
            if (i, total) in memo:
                return memo[(i, total)]
            
            add = dfs(i+1, total+nums[i])
            sub = dfs(i+1, total-nums[i])

            memo[(i, total)] = add+sub

            return add+sub

        return dfs(0, 0) 
