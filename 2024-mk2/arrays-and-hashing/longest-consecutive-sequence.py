"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.
"""

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in numSet:
            if n-1 not in numSet:
                length = 0
                curr = n
                while curr+length in numSet:
                    length += 1
                res = max(res, length)
        return res

sol = Solution()
print(sol.longestConsecutive([0,3,2,5,4,6,1,1]))

