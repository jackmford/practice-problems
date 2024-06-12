"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                return m

        if target < nums[m]:
            return m
        else:
            return m+1
  
sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))
print(sol.searchInsert([1,3,5,6], 2))
print(sol.searchInsert([1,3,5,6], 7))
