class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        combo = []
        res = []
        # Sorting lets us find dupes
        candidates = sorted(candidates)

        def dfs(i, total):
            if total == target:
                res.append(combo[:])
                return
            if i > len(candidates)-1:
                return
            # Don't continue down a path if our total is too high, anything below will be useless to explore
            if total > target:
                return
            
            # Left side
            combo.append(candidates[i])

            # No reason to check anything that is greater than our target
            dfs(i+1, total+candidates[i])

            combo.pop()

            # Right side avoid dupes that we've already processed on the left side
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            dfs(i+1, total)

        dfs(0, 0)
        return res
            
        
