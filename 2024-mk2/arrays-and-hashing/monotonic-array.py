"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""

from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # Check increasing
        increasing = True
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                increasing = False

        # Check decreasing
        decreasing = True
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                decreasing = False

        if decreasing == False and increasing == False:
            return False
        return True



sol = Solution()
print(sol.isMonotonic([1,2,2,3]))
print(sol.isMonotonic([1,3,2]))
