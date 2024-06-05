"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""

from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        # Check monotone increasing
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                increasing = False

        decreasing = True
        # Check monotone decreasing
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                decreasing = False

        if increasing == True or decreasing == True:
            return True
        return False

sol = Solution()
print(sol.isMonotonic([1,2,2,3]))
print(sol.isMonotonic([1,3,2]))
