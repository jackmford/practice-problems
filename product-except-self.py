from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      answer = []
      ctr = 0
      total = 1
      for i in range(len(nums)):
        tmp = nums
        tmp.pop(i)
        print(nums)
        #print(nums[i:])
        ##if i != ctr:
          #total *= nums[i]
        
      return 

sol = Solution()
sol.productExceptSelf([1, 2, 3, 4])
