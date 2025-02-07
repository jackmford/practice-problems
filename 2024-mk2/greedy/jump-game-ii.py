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

class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        l, r = 0, 0

        while r < len(nums)-1:
            farthest = 0

            for i in range(l, r+1):
                # i +nums[i] == the farthest you can jump
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res += 1

        return res
        



