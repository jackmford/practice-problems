class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1,1

        for n in nums:
            tmp = curMin
            curMin = min(n*curMin, n*curMax, n)
            curMax = max(n*tmp, n*curMax, n)

            res = max(res, curMax)

        return res
