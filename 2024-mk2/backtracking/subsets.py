class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        # For every num (i) there are two choices. Add the num[i], or do not.
        def dfs(i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            print(subset)
            subset.append(nums[i])
            dfs(i+1)

            print(subset)
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res
        
