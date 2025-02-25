class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        nums = []
        res = []
        def dfs(j):
            if len(nums)==k:
                res.append(nums[:])

            for i in range(j, n+1):
                nums.append(i)
                dfs(i+1)
                nums.pop()
            
            return
        dfs(1) 
        return res
                
