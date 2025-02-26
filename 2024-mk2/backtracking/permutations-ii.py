class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Approach:
        # any index i can be any of the numbers, so we need to go through each number at each recursion level
        # but, getting to a new index i, we dont want to use a number that's already in the subarray
        # unique IDs should be stored as tuples of (index, value) to avoid getting messed up from duplicates

        # Base case:
        # subset length == len(nums)

        # When we return from a call, we need to remove from the hash set
        used = set()
        completed_sets = set()
        subset = []
        res = []

        def dfs():
            if len(nums) == len(subset) and tuple(subset) not in completed_sets:
                res.append(subset[:])
                completed_sets.add(tuple(subset[:]))
                return

            for j in range(len(nums)):
                if j not in used:
                    print(used)
                    subset.append(nums[j])
                    used.add(j)
                    dfs()
                    subset.pop()
                    used.remove(j)
        
        dfs()
        return res
