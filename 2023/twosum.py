from typing import List

#class Solution:
#  def twoSum(self, nums: List[int], target:int) -> List[int]:
#    sol = []
#    for i in range(len(nums)):
#      for j in range(i+1, len(nums)):
#        print(nums[i] + nums[j])
#        if nums[i] + nums[j] == target:
#          sol.append(i)
#          sol.append(j)
#          return sol
#    return []

class Solution:
  def twoSum(self, nums: List[int], target:int) -> List[int]:
    hashMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[n] = i
    return

sol = Solution()
final = sol.twoSum([2, 5, 5, 11], 10)
print(final)
