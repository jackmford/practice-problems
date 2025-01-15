        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        targ = sum(nums)//2
        def dfs(i, total):
            if i >= len(nums):
                if total == targ:
                    return True
                return False
            if total > targ:
                return False
            
            # Choose
            c = dfs(i+1, total+nums[i])
            # Don't choose
            d = dfs(i+1, total)

            return c or d

        return dfs(0, 0)
        
