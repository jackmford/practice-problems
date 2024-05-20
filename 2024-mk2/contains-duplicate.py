from typing import List

"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if d.get(n) != None:
                return True
            d[n] = 0
        return False

sol = Solution()
nums = [1, 2, 3, 3]
print(sol.hasDuplicate(nums))
