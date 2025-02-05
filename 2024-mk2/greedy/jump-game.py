# top down memoized
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

# greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        targ = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            # From where we are, we can get where we need to go to get to end
            if i + nums[i] >= targ:
                targ = i
        return targ == 0
