class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = {}
        def dfs(i):
            if i + nums[i] >= len(nums)-1:
                return True
            if i in memo:
                return memo[i]

            for j in range(i+1, i+nums[i]+1):
                if nums[j] > 0 and dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return dfs(0)
