from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      # Kadane's Algorithm
      maximum = min(nums)
      cur_total = 0 

      for num in nums:
        cur_total += num
        if maximum < cur_total:
          maximum = cur_total
        if cur_total < 0:
          cur_total = 0 

      return maximum

sol = Solution()
print(sol.maxSubArray([5, 4, -1, 7, 8]))
