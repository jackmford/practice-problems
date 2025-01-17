"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""

from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        s = s.split(" ")
        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] in d.keys() and d[pattern[i]] != s[i]:
                return False
            elif s[i] in d.values() and pattern[i] not in d.keys():
                return False
            d[pattern[i]] = s[i]

        return True


sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))
print(sol.wordPattern("abba", "dog cat cat fish"))
print(sol.wordPattern("aaaa", "dog cat cat fish"))
