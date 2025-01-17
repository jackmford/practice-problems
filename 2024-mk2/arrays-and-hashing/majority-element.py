"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
                count += 1
            elif n != res:
                count -=1
            else:
                count +=1

        return res

sol = Solution()
print(sol.majorityElement([3,2,3]))
