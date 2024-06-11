"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1

        while j<len(nums):
            if nums[j] == nums[i]:
                j+=1
            elif nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
        print(nums)
        return i+1


sol = Solution()
print(sol.removeDuplicates([1,1,2]))
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
