"""
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l,r = 0,1
        res = 1
        while r < len(s):
            if s[r] in s[l:r]:
                l+=1
            else:
                r+=1
                res = max((r-l), res)
        return res

sol = Solution()
print(sol.lengthOfLongestSubstring("zxyzxyz"))
print(sol.lengthOfLongestSubstring("xxxx"))
print(sol.lengthOfLongestSubstring("abcabcbb"))

