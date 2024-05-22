"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            print(res[i], prefix)
        print(res)
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        #res = [n for n in nums]
        #pre = [n for n in nums]
        #post = [n for n in nums]
        #for i in range(1, len(nums)):
        #    pre[i] = pre[i]*pre[i-1]

        #for i in range(len(nums)-2, -1, -1):
        #    post[i] = post[i]*post[i+1]

        #for i in range(len(nums)):
        #    if i == 0:
        #        res[i] = post[i+1]
        #    elif i == len(nums)-1:
        #        res[i] = pre[i-1]
        #    else:
        #        res[i] = pre[i-1]*post[i+1]


        #print(pre)
        #print(post)
        return res

sol = Solution()
#print(sol.productExceptSelf([4,3,2,1,2]))
print(sol.productExceptSelf([1,2,3,4]))
