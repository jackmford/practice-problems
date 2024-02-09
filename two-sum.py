from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for index, num in enumerate(nums):
            if target-num in m:
                return m[target-num], index 
            else:
                m[num] = index
        
        
sol = Solution()