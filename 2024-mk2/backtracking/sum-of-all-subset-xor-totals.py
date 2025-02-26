class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []
        res = 0
        def dfs(i):
            nonlocal res

            if len(subset) > 0:
                xor_sum = 0
                for n in subset:
                    xor_sum = xor_sum ^ n
                res+=xor_sum
            
            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j+1)
                subset.pop()

        dfs(0)
        return res
        
