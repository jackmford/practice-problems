class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # for every candidate, add itself until you go too far or find it equals target
        # when this happens,
        # pop the last number off,
        # move to the next number to try
        combo = []
        res = []
        def dfs(i):
            if sum(combo) == target:
                res.append(combo[:])
                return
            if i >= len(candidates) or sum(combo) > target:
                return

            combo.append(candidates[i]) 
            dfs(i)

            combo.pop()
            dfs(i+1)



        dfs(0)
        return res


