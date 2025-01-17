"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i] == nums[j]:
                    res += 1
        return res

sol = Solution()
print(sol.numIdenticalPairs([1,2,3,1,1,3]))
