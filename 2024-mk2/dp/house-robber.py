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



 class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can either rob a house and skip the next
        # or we can skip the current and move to the next
        memo = {}
        def rob(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            take = nums[i] + rob(i+2)
            skip = rob(i+1)

            memo[i] = max(take, skip)
            return memo[i]

        return rob(0)
               
