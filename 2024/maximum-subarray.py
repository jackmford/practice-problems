class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSome = 0

        for n in nums:
            if curSome < 0:
                curSome = 0
            curSome += n
            maxSub = max(curSome, maxSub)
        return maxSub
