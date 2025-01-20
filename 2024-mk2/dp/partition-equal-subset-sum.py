class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Basically need a path that adds up to sum(nums)//2
        if sum(nums) % 2 != 0:
            return False
        half = sum(nums)//2 
        print(half)
        # Can choose/not choose a number
        memo = [[-1]*(half+1) for _ in range(len(nums)+1)]
        def dfs(total, i):
            print(total)
            if total == half:
                return True
            if total > half:
                return False
            if memo[i][total] != -1:
                return memo[i][total]
            
            pick = False
            dont = False
            if i < len(nums):
                # Pick
                pick = dfs(total+nums[i], i+1)
                # Dont pick
                dont = dfs(total, i+1)

            memo[i][total] = pick or dont
            return pick or dont
        
        return dfs(0, 0)


