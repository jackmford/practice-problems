"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
"""

from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j = 0,0

        if len(s) == 0:
            return 0

        g = sorted(g)
        s = sorted(s)
        res = 0
        while i<len(g) and j<len(s):
            if s[j] >= g[i]:
                res +=1
                j+=1
                i+=1
            else:
                j+=1
        return res

sol = Solution()
print(sol.findContentChildren([1,2,3], [1,1]))
print(sol.findContentChildren([1,2], [1,2,3]))
print(sol.findContentChildren([10,9,8,7], [5,6,7,8]))

