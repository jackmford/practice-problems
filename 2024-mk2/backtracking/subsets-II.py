
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        sub = []
        nums = sorted(nums)

        def dfs(i):
            if i == len(nums):
                res.append(sub[:])
                return
            
            # Always include item we are on
            sub.append(nums[i])
            dfs(i+1)
            # Remove it (look at other paths)
            sub.pop()

            # Don't go down a path if that num has already been explored to avoid duplicates
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            dfs(i+1)

        dfs(0)
        return res
        
