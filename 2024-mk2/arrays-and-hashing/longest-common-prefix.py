"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        min_len = len(strs[0])
        for word in strs:
            min_len = min(min_len, len(word))
        
        i = 0
        res = ""

        while i < min_len:
            char = strs[0][i]

            for word in strs:
                if word[i] != char:
                    return res

            res += char
            i+=1

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
