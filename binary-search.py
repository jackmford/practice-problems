from math import floor
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums)-1
        while i <= j:
            mid = i+(j-i) // 2
            if nums[mid] != target:
                if nums[mid] < target:
                    i = mid+1
                elif nums[mid] > target: 
                    j = mid-1
            else:
                return mid
        
        return -1

sol = Solution()
print(sol.search([-1,0,3,5,9,12], -1))