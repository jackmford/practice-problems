from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, k-1
        if len(nums)==1:
            return nums[0]-nums[0]
        res = float("INF")
        num_list = sorted(nums)
        print(num_list)
        while r<len(nums):
            res = min(res, abs(num_list[r]-num_list[l]))
            l+=1
            r+=1
        
        return res
sol = Solution()
print(sol.minimumDifference([5,4,2,1,3], 2))
print(sol.minimumDifference([9,4,1,7],2))
