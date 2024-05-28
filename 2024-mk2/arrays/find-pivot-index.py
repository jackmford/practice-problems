"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]*len(nums)
        postfix = [0]*len(nums) 

        prefixctr = 0
        for i in range(1, len(nums)):
            prefixctr += nums[i-1]
            prefix[i] = prefixctr

        postfixctr = 0 
        for i in range(len(nums)-2, -1, -1):
            postfixctr += nums[i+1]
            postfix[i] = postfixctr

        for i in range(len(prefix)):
            if prefix[i] == postfix[i]:
                return i

        return -1

sol = Solution()
sol.pivotIndex([1,7,3,6,5,6])

