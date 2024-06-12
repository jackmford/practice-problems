"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""

from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, 1

        while j<len(nums):
            if nums[i]%2 == 1 and nums[j]%2 == 1:
                j+=1
            elif nums[i]%2 == 1 and nums[j]%2 == 0:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i+=1
                j+=1
            else:
                i+=1
                j+=1

        return nums
sol = Solution()
print(sol.sortArrayByParity([3,1,2,4]))
print(sol.sortArrayByParity([3,2,2,4]))
print(sol.sortArrayByParity([1, 2, 3, 5,2,2,4]))
