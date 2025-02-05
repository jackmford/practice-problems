# top down recursive memoized
class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}
        def dfs(i):
            if i >= len(nums)-1:
                return 0
            if i in memo:
                return memo[i]
    
            res = float("inf")
            for j in range(i+1, i+nums[i]+1):
                if j > 0:
                    res = min(res, 1 + dfs(j))
            memo[i] = res
            return res
        return dfs(0)

