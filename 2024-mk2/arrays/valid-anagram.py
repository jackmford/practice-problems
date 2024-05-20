"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = defaultdict(int)
        dd = defaultdict(int)
        for char in s:
            d[char] += 1
        for char in t:
            dd[char] += 1

        for k,v in d.items():
            if d[k] != dd[k]:
                return False
        return True

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
