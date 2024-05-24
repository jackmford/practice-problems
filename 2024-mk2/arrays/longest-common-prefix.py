"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = len(strs[0])
        prefix = ''
        for word in strs:
            if len(word) < min:
                min = len(word)
        i = 0
        prefix = ''
        while i < min:
            c = strs[0][i]
            for word in strs:
                if word[i] != c:
                    return prefix
            prefix+=strs[0][i]
            i+=1

        return prefix

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
