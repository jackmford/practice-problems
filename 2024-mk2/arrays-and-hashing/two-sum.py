"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""
from typing import List
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d ={}
        for i in range(len(nums)):
            dist = target-nums[i]
            if d.get(dist) != None:
                return [d[dist], i]
            else:
                d[nums[i]] = i
        return []

sol = Solution()
print(sol.twoSum([3,4,5,6], 7))



