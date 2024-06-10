"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1

        while j < len(nums):
            print(i, j)
            if nums[i] == 0 and nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
                i+=1
                j+=1
            elif nums[i] == 0 and nums[j] == 0:
                j+=1
            else:
                i+=1
                j+=1

        return nums

sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))
print(sol.moveZeroes([4,1,0,3,12]))
print(sol.moveZeroes([3,1,0,0,12]))
