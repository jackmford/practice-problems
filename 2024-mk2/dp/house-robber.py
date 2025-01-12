class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        robbed = []
        memo = [-1] * len(nums)

        def dfs(i):
            nonlocal res
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]

            rob = nums[i] + dfs(i+2)
            skip = dfs(i+1)

            memo[i] = max(rob, skip)

            return max(rob, skip)

        return dfs(0)



        
