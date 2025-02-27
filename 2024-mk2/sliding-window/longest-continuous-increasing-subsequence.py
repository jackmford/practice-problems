class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l, r = 0, 1
        res = 1
        while r < len(nums):
            if nums[r] > nums[r-1]:
                res = max(res, r-l+1)
                r+=1
            else:
                l = r
                r+=1
        return res
