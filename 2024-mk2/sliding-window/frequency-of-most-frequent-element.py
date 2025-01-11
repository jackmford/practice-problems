class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        l,r = 0,0
        res = 0
        total = 0

        while r < len(nums):
            total+=nums[r]

            # Check for validity
            while (r-l+1)*nums[r] - total > k:
                total-=nums[l]
                l+=1
            
            res = max(res, (r-l+1))
            r+=1
        return res

