"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        prefarr = [0]*len(nums)
        pref = 0
        for i in range(len(nums)):
            pref+=nums[i]
            prefarr[i] = pref

        self.nums = prefarr
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.nums[right]-self.nums[left-1]
        else:
            return self.nums[right]-0

        


# Your NumArray object will be instantiated and called as such:
nums = [-2,0,3,-5,2,-1]
obj = NumArray(nums)
left = 0
right = 2
param_1 = obj.sumRange(left,right)
print(param_1)
