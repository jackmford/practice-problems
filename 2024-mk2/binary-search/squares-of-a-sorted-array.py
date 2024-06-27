"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2

        l,r = 0, len(nums)-1
        while l <=r:
            m = (r+l) // 2
            if nums[m] < nums[l]:
                tmp = nums[l]
                nums[l] = nums[m]
                nums[m] = tmp
                l = m
            elif nums[m] > nums[r]:
                tmp = nums[r]
                nums[r] = nums[m]
                nums[m] = tmp
                r = m
            else:
                l+=1
        return nums




sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))
print(sol.sortedSquares([-7,-3,2,3,11]))
