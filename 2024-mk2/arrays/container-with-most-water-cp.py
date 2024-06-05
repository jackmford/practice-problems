"""
You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""

from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1
        while l<r:
            height = min(heights[l], heights[r])
            res = max(res, height*(r-l))
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return res

sol = Solution()
print(sol.maxArea([1,7,2,5,4,7,3,6]))
