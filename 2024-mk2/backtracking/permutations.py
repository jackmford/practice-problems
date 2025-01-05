class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # For every level,
        # Need to add all unused numbers
        # Recursive looping at each level
        res = []
        permutations = []
        used = [False]*len(nums)

        def dfs():
            if len(permutations) == len(nums):
                res.append(permutations.copy())
                return
            
            # At every level, this will generate all combos of unused numbers
            for i in range(len(nums)):
                # If at this level, number is not used,
                # use it, mark as used, search more combos
                if used[i] == False:
                    permutations.append(nums[i])
                    used[i] = True
                    dfs()
                    permutations.pop()
                    used[i] = False
                
        dfs()
        return res
        
