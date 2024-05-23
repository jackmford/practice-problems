"""
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
"""

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            windowSize = r-l+1

            if windowSize - max(count.values()) > k: # we can't have anymore substitutions
                count[s[l]]-=1
                l+=1
            res = max(windowSize, res)
        return res

sol = Solution()
print(sol.characterReplacement("XYYX", 2))
print(sol.characterReplacement("AAABABB", 1))
print(sol.characterReplacement("AABABBA", 1))
